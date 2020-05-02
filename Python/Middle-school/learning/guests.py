name = ''
while not name: #(1)
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: #(2)
    print('Be sure to have enough room for all your guests.') #(3)
print('Done')
