password = ''
print('what is your name')
name = input().lower()
if name == 'yahya':
    password = '0'   
if password:
    print('access granted yahya')
else:
    print('what is the password?')
    password = input()
    if password >= '1':
        print('what is the password')
        passw = input()
        if passw == '1234': 
            print('access granted')
        else:
            print('wrong password.')
            print('use numbers')
            print()
            print('what is the password')
            passw = input()
  

        
           
