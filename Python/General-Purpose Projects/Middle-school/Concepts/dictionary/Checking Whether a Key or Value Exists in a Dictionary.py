spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())
print('Zophie' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)
#In the previous example, notice that 'color' in spam is essentially a shorter version of writing 'color' in spam.keys()().
#This is always the case: If you ever want to check whether a value is (or isn’t) a key in the dictionary, you can simply use the in (or not in)
#keyword with the dictionary value itself.
