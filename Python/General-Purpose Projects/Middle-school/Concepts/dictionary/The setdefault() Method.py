spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

#The setdefault() Method
pam = {'name': 'Pooka', 'age': 5}
pam.setdefault('color', 'black')
print(pam)

pam.setdefault('color', 'white')
print(pam)
#The first time setdefault() is called, the dictionary in spam changes to {'color': 'black', 'age': 5, 'name': 'Pooka'}.
#The method returns the value 'black' because this is now the value set for the key 'color'.
#When spam.setdefault('color', 'white') is called next, the value for that key is not changed to 'white' because spam already has a key named 'color'.
