while True:
  print('Who are you?')
  name = input()
  if name != 'yahya':     #(1)
    continue              #(2)
  print('Hello, yahya. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)
