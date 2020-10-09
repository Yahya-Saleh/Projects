import re

# Match the phone numbers
with open("data.txt") as f:
    data = f.read()

pattern = re.compile(r"(\d{3}[. -]){2}\d{4}")
matches = pattern.finditer(data)

for match in matches:
    print(match.group())
