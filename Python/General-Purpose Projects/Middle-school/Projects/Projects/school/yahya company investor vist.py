#import commands
import random
import time
import sys

def displayintro():
    #import commands
    import random
    import time
    import sys

    #hook
    print('welcome to RDC (Robot Design Community)')
    print('')
    print('before we start. let me ask you')
    time.sleep(3)
    print('have you ever wanted to change the world?')
    time.sleep(3)
    print('')
    print('well if you have then our company is the best place for you to invest')
    time.sleep(3)
    print('')
    print('ROBOTs, maybe you think this idea is more of a fiction than reality')
    print(',but our company RDC (Robot Design Community) is going to put this idea to life')
    time.sleep(3)
    print('')
    print('here in our company we are producing diffrent types of robots to chnage the world')


def hischoice():
    #import commands
    import random
    import time
    import sys

    while True:
        print()
        print('are you Convinced?')
        print('do  you want to know more?')
        print()
        print('(press yes to know about the invest options')
        print('or press no if you want to return to the information part.)')
        hischoice = input().lower()
        if hischoice == 'yes':
            invest()
        elif hischoice == 'no':
            chooseinfo()
        else:
            print('please choose yes or no.')
            print()
            continue
        
#main info. def
def chooseinfo():
    #import commands
    import random
    import time
    import sys
    
    info = ''
    while True:
        
        print('mr.'  + str(hisname) + ' , sice that you intrested in our company')
        print('what do you want to know about our company?')
        print('( (1)VP, (2)problem solved, (3)bundle benefits, (4)newness, (5)customer needs, (6)performance, (7)customization, or(8)price)')
        info = input().lower()
        print()
        
        if info == 'vp' or info == '1':
                print('of course, having robots in the markets will provide insane value to our custmers(VP)')
                print('people may think that their life is good and easy')
                print(', but our product will make them realise a new need that they never thought of')
                hischoice()
                #relate to newness
                        
        if info == 'customer needs' or info == 'cn' or info == '5':
            print('With the new idea of robots')
            print('we are going to make people realize a needthey didn’t now (newness) .')
            print('As the robots will help people with there daily lives.')
            hischoice()

        elif info == 'bundle benefits' or info == 'bb' or info == '3':
            print('Our robots designs would include as much bundle usage as possible. ')
            print('Because we want our customer to get as much benefits as possible from our robots')
            hischoice()
            
        elif info == 'problem solved' or info == 'ps' or info == '2':
            print('Robots will provide help in your daily life. ')
            print('especially if you don’t like simple, but numerous work')
            print(', or your age can’t help you finish them')
            hischoice()
        elif info == 'newness' or info == 'n' or info == '4':
            print('We are creating a new world ')
            print('where robots will help humans develop and progress ')
            hischoice()
        elif info == 'performance' or info == 'p' or info == '6':
            print('We do our best to improve our products and service. ')
            print('With an easy access to these improvement')
            hischoice()

        elif info == 'customization' or info == 'c' or info == '7':
            print('Here in our company you get to design, and color your robot to the way it suits you')
            hischoice()

        elif info == 'price' or info == 'pr' or info == '8':
            print('We are doing our best to make shore to provide the best quality with the lowest value ')
            hischoice()
            
def invest():
    while True:
        print('mr.' + hisname + ', how do you want to invest with resources ,or finance.')
        print('you can press exit to return to the information part.')
        print('(by typing one of the following invest options')
        print('you get to  know about the available types.)')
        invest = input()
        if invest == 'resources' or invest == 'r' or invest == '1':
            resources()
        elif invest == 'exit':
            print('please wait...')
            time.sleep(2)
            chooseinfo()

        elif invest == 'finance' or invest == 'f' or invest == '2':
            finance()

    
            
def resources():
    #import commands
    import random
    import time
    import sys

    while True:
        print('here are some time options.')
        print('(you can type exit to go to the invest options)')
        print('1-programs for the robot')
        print('2-Human resources')
        print('3-Resources to make the physical body of the robot')
        resources = input()
        if resources == 'programs for the robot' or resources == 'pr' or resources == '1':
            print('programs for the robot:-')
            print()
            print(' the offer in return:')
            print('     1-30% of our profits')
            print('     2-test the robot')
            print('     3-may take one robot for free')
            print()
            print(' Legal consideration(research-based):')
            print('     1-If a problem comes from the programs he will be held responsible') 
            print('     2-if it was working and we misused it we will be held responsible')
            print('     3- the robot of this program will be named by you')
            print()
            while True:
                print('are you Convinced?')
                print('do you want to invest in this option?')
                print('(if you type no you will return to the time options.)')
                choose = input()
                if choose == 'yes':
                    print('thank you mr.' + hisname + ' for invesing in this option.')
                    print('we hope that both of us will benfite from this decision')
                    print('')
                    print('do you want to leave a comment?')
                    comment = input()
                    print('thank you mr.' + hisname)
                    sys.exit()
                elif choose == 'no':
                    resources()
        elif resources == 'exit':
            print('please wait...')
            time.sleep(2)
            invest()
            
        elif resources == 'hr' or resources == 'human resouces' or resources == '2':
            print('human resources:-')
            print()
            print(' the offer in return:')
            print('     1-He will be held responsible for those workers actions.')
            print('     2-They must be trained to the job')
            print()
            print(' Legal consideration(research-based):')
            print('     1-16% Of our profits')
            print('     2- may take one robot for free')
            print()
            while True:
                print('are you Convinced?')
                print('do you want to invest in this option?')
                print('(if you type no you will return to the time options.)')
                choose = input()
                if choose == 'yes':
                    print('thank you mr.' + hisname + ' for invesing in this option.')
                    print('we hope that both of us will benfite from this decision')
                    print('')
                    print('do you want to leave a comment?')
                    comment = input()
                    print('thank you mr.' + hisname)
                    sys.exit()
                elif choose == 'no':
                    resources()
        elif resources == 'Resources to make the physical body of the robot' or resources == 'pb' or resources == '3':
            print('Resources to make the physical body of the robot:-')
            print()
            print(' the offer in return:')
            print('       1-If the quality is really bad he must change them. ')
            print('       2-we will be held responsible if misused. ')
            print('       3- you don’t get the right to name the robot')
            print(' Legal consideration(research-based):')
            print('       1-30% of our profits')
            print('       2-we will accept ideas about the structure of the robot ')
            print()
            while True:
                print('are you Convinced?')
                print('do you want to invest in this option?')
                print('(if you type no you will return to the time options.)')
                choose = input()
                if choose == 'yes':
                    print('thank you mr.' + hisname + ' for invesing in this option.')
                    print('we hope that both of us will benfite from this decision')
                    print('')
                    print('do you want to leave a comment?')
                    comment = input()
                    print('thank you mr.' + hisname)
                    sys.exit()
                elif choose == 'no':
                    resources()

def finance():
    #import commands
    import random
    import time
    import sys
    while True:
        print('here are some time options.')
        print('(you can type exit to go to the invest options)')
        print('1-1,000,000$')
        print('2-2,000,000 or more')
        finance = input()

        if finance == '1' or finance == '1,000,000$':
            print('1,000,000$:-')
            print('   we offer in return:')
            print('        1-40% of our profits.')
            print('        2-you may get one of our products for free (to try and rate it).')
            print()
            print('   Legal consideration(research-based)')
            print('         1-If the project fail he gets 47% of what he paid.')
            print('         2-you can help in the project, but you don’t own it')
            print()
            while True:
                print('are you Convinced?')
                print('do you want to invest in this option?')
                print('(if you type no you will return to the time options.)')
                choose = input()
                if choose == 'yes':
                    print('thank you mr.' + hisname + ' for invesing in this option.')
                    print('we hope that both of us will benfite from this decision')
                    print('')
                    print('do you want to leave us a comment?')
                    comment = input()
                    print('thank you mr.' + hisname)
                    sys.exit()
                elif choose == 'no' or choose == 'n':
                    finance()
            
        
        elif finance == 'exit':
            print('please wait...')
            time.sleep(2)
            invest()

        elif finance == '2' or finance == '2,000,000 or more':
            print('2,000,000 or more:-')
            print('   we offer in return:')
            print('        1-50% of our profits.')
            print('        2-you may get one of our products for free (to try and rate it).')
            print()
            print('   Legal consideration(research-based)')
            print('         1-If the project fail he gets 52% of what he paid.')
            print('         2-you can help in the project, but you don’t own it')
            print()
            while True:
                print('are you Convinced?')
                print('do you want to invest in this option?')
                print('(if you type no you will return to the time options.)')
                choose = input()
                if choose == 'yes':
                    print('thank mr.' + hisname + ' you for invesing in this option.')
                    print('we hope that both of us will benfite from this decision')
                    print('')
                    print('do you want to leave us a comment?')
                    comment = input()
                    print('thank you mr.' + hisname)
                    sys.exit()
                elif choose == 'no' or choose == 'n':
                    finance()
            
#the start of the program:-
            
#import commands
import random
import time
import sys

#the basic intro.        
print('RDC (Robot Design Community)')
print('presents..')
print()
print('the following program is for those who are welling to invest in our company if Convinced')
time.sleep(4)
print()

displayintro()

#asks for his name
print('if you are interested in our company')
print('kindly can you enter your name?')
hisname = input()

chooseinfo()
            

     


    
    
