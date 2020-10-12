print("hello world")
yourname=str(input('what is your name?'))
print('welcome to the RDC '+ yourname)
print('Robot Design Company ')
print("the length of your name is")
print(len(yourname))
parsed = False
while not parsed:
    try:
        yourage=int(input("what is your age?"))
        parsed= True
    except ValueError:
        print("please input a number")
if yourage<=15:
    print("you are too young to be here, sorry")
else:
    print(yourname+" ,have you ever thought that it is possable to obtain a robot?")
    print('(please use low cause letters)')
    A=str(input())
    print('then it is your lucky day')
    print('here we offer the best robots')
    print('as you get to choose ,and design your own')
    en=input()
