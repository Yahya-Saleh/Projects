#the Guess My Number program (GMN)

#the import modules
import random
import sys
import time

#the first introduction
def basicintro():
    import time
    
    print('Yahya Sherif presents...the GMN')
    for i in range(5):
        print(5-i)
        time.sleep(1)
        
#what is his name
def hisname():
    global hisname
    
    print('Welcome challenger, what is your name?')
    hisname = input()

    print()
    
#the description of the game
def description():
    import time
    
    print()
    print('Welcome ' + hisname + ' to Guess My Number (GMN),')
    time.sleep(1)
    
    print()
    print(' In this game, I get to pick a number between two numbers that you will choose and you get to guess it.')
    time.sleep(2)
    
    print()
    print('So for example, I will ask you what is the first number, and once you have inputed it I will ask you ')
    print('for the second number. Also, you get to pick how many chances you have.')
    time.sleep(3)
    
    print(' ')
    print("Once you guess if I tell you 'Too close, but still high’, then that means that your guess is just in ")
    print("range of 1 to 10 above the answer.")
    time.sleep(2)

    print()
    print("Likewise, if I tell you 'Too close, but still low', then that means ")
    print("that your guess is just in range of 1 to 10 blow the answer. Also, if I told you 'Too low', or 'Too high'")
    print(", then that means that your guess is out of the range (+10 ,or -10) of the correct answer.")
    print("")
    time.sleep(3)
    
    print("Press 'ENTER' to continue")
    con = input()

#the range of the random int1
def rangerandint1():
    global x
    
    try:
        while True:
            print(hisname + ' enter the first number of the two numbers that I will pick between.')
            x = input()
            
            if int(x) > 0:
                rangerandint2()

            elif int(x) <= 0:
                rangerandint2()
                
            else:
                print(hisname + ' please input a number')

    except ValueError:
        print(hisname + ' please input a number')
        print()
        r()
def r():
    rangerandint1()
#the range of the random int2
def rangerandint2():
    global y

    try:
        while True:
            print('Now ' + hisname + ' enter the second number of the two numbers that I will pick between.')
            print('(This number must be greater than the first number)')
            y = input()
            
            if int(y) > int(x):
                frange()
                
            else:
                print(hisname + ' please input a number that is greater than your first number')

    except ValueError:
        print(hisname + ' please input a number that is greater than your first number')
        print('')
        r2()    

def r2():
    rangerandint2()

def frange():
    global z

    try:
        while True:
            print(' Final ' + hisname + ' pick the number of chances you want to have.')
            z = int(input())

            if int(z) > 0:
                intro()

            else:
                print('Please input a positive number')
    except ValueError:
        print('Please input a positive number')
        print()
        r3()

def r3():
    frange()
    
#the start of the game
def intro():
       
    global Answer
    
    Answer = random.randint(int(x),int(y))

    print('..................................')
    print('now let me think of a number')
    print('hum..hum')
    for i in range(3):
        print(random.randint(int(x),int(y)))
        print(random.randint(int(x),int(y)))
        time.sleep(1)

    print('........................................')
    print('Okey')
    print('I think of a number between ' + x + ' and ' + y + '.')
    takeaguess()
    
#take your guess
def takeaguess():
    import time
    import random
    
    global outcome

    for i in range(z):
        print()
        print('Take a guess ' + hisname + ' you have ' + str(z - i) + ' chances left.')
        print('(you can input give up if you give up)')  
        outcome = input()

        try:
            #did he give up?
            if outcome == 'give up' or outcome == 'gu':
                print('........................................')
                print('The number I chose ' + hisname + ' is ' + str(Answer))
                print('Please wait')
                for i in range(3):
                    print(3 - i)
                    time.sleep(1)
                again()
        
            elif int(outcome) == Answer:
                print()
                print('Good job,' + hisname + ' you guessed the number.')
                again()

            elif int(outcome) > Answer + 10:
                print('Too high')

            elif int(outcome) < Answer - 10:
                print('Too low')

            elif int(outcome) < Answer and  int(outcome) >= Answer - 10:
                print('Too close, but still low')

            elif int(outcome) > Answer and int(outcome) <= Answer + 10:
                print('Too close, but still high')
            
            else:
                print()
                print('Please input a number between ' + x + ' and ' + y + '.')
                print(" Or input 'give up' if you give up.")
            
        except ValueError:
            print()
            print('Please input a number between ' + x +' and '+ z + '.')
            print(" Or input 'give up' if you give up.")

    print('........................................')
    print('Sorry ' + hisname + ' you lose.')
    print('The number I chose ' + hisname + ' is ' + str(Answer))
    again()
    
#does he want a new game
def again():
    import sys
    import time
    
    while True:
        print('................................')
        print('do you want to play again ' + hisname + '?')
        print('we will get a diffrent number.')
        play = input()

        if play == 'yes' or play == 'y':
            while True: 
                print('same range?' + x + ',' + y)
                st = input()

                if st == 'yes' or st == 'y':
                    print('please wait...')
                    for i in range(3):
                        print(3 - i)
                        time.sleep(1)
                    intro()

                elif st == 'no' or st == 'n':
                    print('please wait...')
                    for i in range(3):
                        print(3 - i)
                        time.sleep(1)
                    rangerandint1()

                else:
                    print(hisname + ' input yes or no')
                    
        elif play == 'no' or play == 'n':
            print('.................................')
            print('thank you ' + hisname + ' for stoping by')
            print('I hope you liked my guess game.')
            print()
            time.sleep(3)
            
            print('Do you have any comments for us?')
            comment = input()
            print('Thank you ' + hisname)
            print('Ending program...')
            for i in range(3):
                print(3 - i)
                time.sleep(1)
            sys.exit()

        else:
            print()
            print('please input yes or no.')

#the start of the progrm
basicintro()

hisname()
            
description()          

rangerandint1()

intro()

