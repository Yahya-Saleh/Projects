import re

# Match all of teh following emails
emails = """
g.o.yahya.sherif@gmail.com
st-001@school.edu.my
rt51@yahoo.com
"""

pattern = re.compile(r"[a-zA-Z0-9_.-]+@[a-zA-z](.[a-zA-Z])+")
matches = pattern.finditer(emails)

for match in matches:
    print(match.group())
