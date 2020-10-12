picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
#Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method.
#Without using get(), the code would have caused an error message
try:
    print('I am bringing ' + str(picnicItems['eggs']) + ' eggs.')
except:
    KeyError: 'eggs'
    print("KeyError: 'eggs'")

