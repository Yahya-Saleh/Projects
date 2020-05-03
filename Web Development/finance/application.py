import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("SELECT * FROM stocks WHERE user_id=? ORDER BY stock_name", session["user_id"])
    # start the total by adding the user's current cash
    total = session["cash"]

    # for every stock
    for row in rows:
        # remove what we don't want to display
        del row["user_id"]
        del row["stock_id"]

        #get the current price
        info = lookup(row["symbol"])
        row["current_price"] = usd(info["price"])

        #calculate net gain
        row["possible_gain"] = usd(info["price"] - row["price"])

        #change the formating of the bought price
        row["price"] = usd(row["price"])

        #calculate the total value of the stock and add it to the grand total
        row["total"] = info["price"] * row["shares"]
        total += row["total"]
        row["total"] = usd(row["total"])

    return render_template("index.html",rows=rows, cash=usd(session["cash"]), total=usd(total))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    #if the request method is POST
    info = lookup(request.form.get("symbol"))
    if not info:
        return apology("Invalid symbol!")

    #check if the user can buy the shares
    price = info["price"] * int(request.form.get("shares"))
    if session["cash"] < price:
        return apology("Can't afford")

    #deduct the price for the user's cash and update the database
    session["cash"] -= price
    db.execute("UPDATE users SET cash=? WHERE id=?;", session["cash"], session["user_id"])
    #save the transaction into the database
    db.execute("INSERT INTO transactions(user_id, symbol, stock_name, shares, price, date, action, total) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
        session["user_id"], info["symbol"], info["name"], int(request.form.get("shares")), info["price"], datetime.now(), "buy", price)

    #check if the user already owns shares of the same stocks that he bought for the same price to update
    doneBefore = db.execute("SELECT shares, price FROM stocks WHERE user_id=? AND symbol=? AND price=?;",
        session["user_id"], info["symbol"], info["price"])
    if not doneBefore:
        db.execute("INSERT INTO stocks(user_id, symbol, stock_name, shares, price) VALUES (?, ?, ?, ?, ?); ",
            session["user_id"], info["symbol"], info["name"], int(request.form.get("shares")), info["price"])
    else:
        db.execute("UPDATE stocks SET shares=? WHERE price=? AND symbol=? AND user_id=?;",
            doneBefore[0]["shares"] + int(request.form.get("shares")), info["price"], info["symbol"], session["user_id"])

    return render_template("buy.html", message=["BOUGHT! Your data is updated!"], href="/", text="Home")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    #getting the transactions in corder
    rows = db.execute("SELECT * FROM transactions WHERE user_id=? ORDER BY date DESC", session["user_id"])

    #for every column
    for row in rows:
        #remove the ids
        del row["user_id"]
        del row["trans_id"]

        #set cash to the right format
        row["price"] = usd(row["price"])
        row["total"] = usd(row["total"])

    return render_template("/history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in and how much cash they hold
        session["user_id"] = rows[0]["id"]
        session["cash"] = rows[0]["cash"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login-register.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    #if the request method is POST we look the symbol's information and if we get it we return it to quoted.html for display
    info = lookup(request.form.get("symbol"))
    if not info:
        return apology("Invalid symbol!")

    message = ["A share of", info["name"], "(" + usd(info["price"]) + ")", "costs", info["symbol"]]
    return render_template("quote.html", message=message, href="/buy", text=", Buy?")


@app.route("/register", methods=["POST"])
def register():
    """Register user"""
    #checking for a valid username
    username = request.form.get("username")
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)
    if not username:
        return apology("Enter a username!", 403)
    elif (len(rows) != 0):
        return apology("Username already exists", 403)

    #checking for a valid password
    password = request.form.get("password")
    confirm = request.form.get("confirmation")
    if (not password or len(password) < 8):
        return apology("Enter a valid password!", 403)
    elif (password != confirm):
        return apology("confirmation did match the password!", 403)

    #adding the username and hashed password to the list, and returning the user to the index route
    db.execute("INSERT INTO users(username, hash) VALUES (?, ?);", username, generate_password_hash(password))
    return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    rows = db.execute("SELECT DISTINCT symbol FROM stocks WHERE user_id=?;", session["user_id"])

    #if method is GET we just send back the list of stocks the user owns shares of
    if request.method == "GET":
        return render_template("sell.html", rows=rows)

    #POST method
    #check for correct symbol
    symbol = request.form.get("symbol")
    if not symbol:
        return(apology("Choose a valid symbol"))

    #check for a valid shares input and the user can afford them
    shares = int(request.form.get("shares"))
    dic = db.execute("SELECT SUM(shares) FROM stocks WHERE user_id=? AND symbol=?;", session["user_id"], symbol)
    av_shares = dic[0]["SUM(shares)"]
    if av_shares < shares:
        return apology("you don't have enough shares!")
    elif shares < 1 or not shares:
        return apology("enter a positive number of shares!")

    #updating the session and database
    info = lookup(symbol)
    session["cash"] += shares * info["price"]
    db.execute("UPDATE users SET cash=? WHERE id=?", session["cash"], session["user_id"])

    #updating the stocks data base
    db.execute("UPDATE stocks SET shares=? WHERE symbol=? AND price=(SELECT MAX(price) FROM stocks WHERE symbol=? AND user_id=?) AND user_id=?",
        av_shares - shares, symbol, symbol, session["user_id"], session["user_id"])
    db.execute("DELETE FROM stocks WHERE price!=(SELECT MAX(price) FROM stocks WHERE symbol=? AND user_id=?) AND symbol=? AND user_id=?",
        symbol, session["user_id"], symbol, session["user_id"])

    #storing the transaction
    db.execute("INSERT INTO transactions(user_id, symbol, stock_name, shares, price, date, action, total) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
        session["user_id"], symbol, info["name"], shares, info["price"], datetime.now(), "sell", shares * info["price"])

    return render_template("sell.html", rows=rows, message=["SOLD! Your data is updated!"], href="/", text="Home")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run()
