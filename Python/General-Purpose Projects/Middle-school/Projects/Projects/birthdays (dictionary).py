birthdays = {'alice': 'apr 1', 'bob': 'dec 12', 'mac': 'mar 4'}

while True:
    print()
    print("Enter a name to get the name's birthday (,or leave it blank to quit)")
    name = input()
    if name == '':
        break

    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
        
    else:
        print("I don't have information about " + name)
        print('what is his birthday?')
        bday = input()
        birthdays[name] = bday
        print('birthday dtabase updated')
