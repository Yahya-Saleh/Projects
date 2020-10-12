'''
isalpha() returns True if the string consists only of letters and is not blank.

isalnum() returns True if the string consists only of letters and numbers and is not blank.

isdecimal() returns True if the string consists only of numeric characters and is not blank.

isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.

istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.'''

print('hello'.isalpha())

print('hello123'.isalpha())

print('hello123'.isalnum())

print('hello'.isalnum())

print('123'.isdecimal())

print('    '.isspace())

print('This Is Title Case'.istitle())

print('This Is Title Case 123'.istitle())

print('This Is not Title Case'.istitle())

print('This Is NOT Title Case Either'.istitle())
