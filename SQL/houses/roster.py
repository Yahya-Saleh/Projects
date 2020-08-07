from sys import argv, exit
from cs50 import SQL

# checking for correct input
if len(argv) != 2:
    print("Usage: python roster.py house_name")
    exit(1)

# getting access to the db
db = SQL("sqlite:///students.db")

# running the query and storing it
result = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", argv[1])

# printing out the results
for row in result:
    if row["middle"]:
        name = row["first"] + " " + row["middle"] + " " + row["last"]
    else:
        name = row["first"] + " " + row["last"]

    print(f"{name}, born {row['birth']}")

exit(0)
