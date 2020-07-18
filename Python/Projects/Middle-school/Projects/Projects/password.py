import sys

NAME = False
AGE = False

for i in range(3):
    print()
    print('kindly enter your name')
    name = input().lower()
    
    if name != 'yahya':
        print('wrong name')
        print('you have (' + str(2 - i) + ') remaining trials ')
        continue
    
    elif name == 'yahya':
        print('hello yahya')
        NAME = True
        break
    
if(NAME != True):
    sys.exit()
    
for i in range(3):
    print()
    print('what is your age?')
    age = input()
    
    if age >= str(17):
        print('wrong age, grannie')
        print('you have (' + str(2 - i) + ') remaining trials ')
        continue
    
    if age <= str(15):
        print('wrong age, kiddo')
        print('you have (' + str(2 - i) + ') remaining trials ')
        continue
    
    elif age == str(16):
        print('welcome yahya of the ' + str(age) + ' years')
        AGE = True
        break
    
if AGE != True:
    sys.exit()

elif AGE == True:

    for i in range(3):
        print('')
        print('what is the password?')
        print('(HINT: who do you favor the most)')
        password = input().lower()   

        if password == 'father' or password == 'dad' or password == 'sherif':
            print('access granted')
            break
        
        else:
            print('wrong passwrod ')
            print('you have (' + str(2 - i) + ') remaining trials ')
            print()
            continue
