from sys import argv, exit
import csv
from cs50 import SQL


# checking for correct input
if len(argv) != 2:
    print("Usage: python import.py file.csv")
    exit(1)

# getting access to the database
db = SQL("sqlite:///students.db")

# opening the csv file
with open(argv[1]) as file:
    # reading the values into a dictionary
    reader = csv.DictReader(file)

    # for each dictionary
    for row in reader:
        # we store a list of the fullname
        name = row["name"].split()
        # if there's only 2 names then the middle name is set to none or null
        if len(name) == 2:
            name.insert(1, None)

        # we insert the data into the table in the db
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                   name[0], name[1], name[2], row["house"], row["birth"])

exit(0)