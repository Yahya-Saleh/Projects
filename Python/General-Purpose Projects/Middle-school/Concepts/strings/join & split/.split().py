print('My name is Simon'.split())

'''By default, the string 'My name is Simon' is split wherever whitespace characters such as the space, tab, or newline characters are found.
These whitespace characters are not included in the strings in the returned list.
can pass a delimiter string to the split() method to specify a different string to split upon.'''

print('MyABCnameABCisABCSimon'.split('ABC'))

print('My name is Simon'.split('m'))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))

