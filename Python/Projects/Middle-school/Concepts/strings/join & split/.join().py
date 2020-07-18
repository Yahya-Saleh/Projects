'''The join() method is useful when you have a list of strings that need to be joined together into a single string value.'''

print(', '.join(['cats', 'rats', 'bats']))

print(' '.join(['My', 'name', 'is', 'Simon']))

print('ABC'.join(['My', 'name', 'is', 'Simon']))

'''Notice that the string join() calls on is inserted between each string of the list argument.
For example, when join(['cats', 'rats', 'bats']) is called on the ', ' string, the returned string is ‘cats, rats, bats’.'''
