# Houses

 Hogwarts is in need of a student database. For years, the professors have been maintaing a CSV file containing all of the students’ names and houses and years. But that file didn’t make it particularly easy to get access to certain data, such as a roster of all the Ravenclaw students, or an alphabetical listing of the students enrolled at the school.

## Import.py

 This program takes in a csv file as input and uploads it to the database. The program accounts for the fact that some characters might not have a middle name and adjusts systematically.

### Usage

```bash
Usage: python import.py file.csv
```

## Roster.py

Prints a list of students for a given house in alphabetical order.

### Usage

```bash
Usage: python roster.py house_name
```
