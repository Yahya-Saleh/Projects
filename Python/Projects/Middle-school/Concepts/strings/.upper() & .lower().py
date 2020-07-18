spam = 'hello world!'
print(spam)

spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

#Note that these methods do not change the string itself but return new string values.
#If you want to change the original string, you have to call upper() or lower() on the string and then assign the new string to the variable where the original was stored.
#This is why you must use spam = spam.upper() to change the string in spam instead of simply spam.upper().

print('hello'.upper().lower().upper())
