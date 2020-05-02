spam = [2, 5, 3.14, 1, -7]
print(spam)

spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

print()

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)

spam.sort()
print(spam)

#You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order. 
#Enter the following into the interactive shell:
spam.sort(reverse=True)
print(spam)

print()

#you cannot sort lists that have both number values and string values in them,
#since Python doesn’t know how to compare these values.
try:
    spam = [1, 3, 2, 4, 'Alice', 'Bob']
    spam.sort()
except TypeError:
    print('TypeError')

print()

#sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings.

spam = ['z', 'A', 'a', 'Z', 'B', 'b', 'C', 'c']
spam.sort()
print(spam)

print()

spam = ['alice', 'zarc', 'Alex', 'Zero']
spam.sort(key=str.lower)
print(spam)

#This causes the sort() function to treat all the items in the list
#as if they were lowercase without actually changing the values in the list.
