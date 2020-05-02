#import modules
import time
import random
import sys

# the Basic introduction of the program
def Basicintroduction():
    #import modules
    import time
    import random
    import sys
    
    print('RDC(Robot Design Company) presents...')
    print('the FBP(the Full Business Program)')
    for a in range(5):
        print('      ' + str(5 - a))
        time.sleep(1)

    for b in range(500):
        print('      ' + str(500 - b))

# the main introduction of the program
def introduction():
    #import modules
    import time
    import random
    import sys

    print()
    print('welcome ' + hisname + " to the FBP(the Full Business Program) made by RDC(Robot Design Company)")
    time.sleep(2)
    print('in this program you get to know everything you can know about our company')
    print('the Robot Design Company')
    print()
    time.sleep(3)
    print('the purpose of this program is')
    print('to get you ' + hisname + ' to know more about our company')
    print('and leave us your feed back on how to improve')
    time.sleep(3)
    print('')
    print('press ENTER to continue')
    con = input()
    print('please wait...')
    for c in range(3):
        print(str(3 - c))
        time.sleep(1)
        
    Mainintersection1()

#the origenal intersection
def Mainintersection1():
    #import modules
    import time
    import random
    import sys
    
    print()
    print(hisname + ' here are the nine components of our business')
    
    while True:
        print('which one do you want to know about first')
        print("input it's number")
        print(' 1-Value Proposition')
        print(' 2-Customer Segment(s)')
        print(' 3-Channels of Communication')
        print(' 4-Customer Relationships ')
        print(' 5-Key Activities')
        print(' 6-Key Resources')
        print(' 7-Key Partners')
        print(' 8-Cost Structure')
        print(' 9-Revenue Stream')
        start = input()

        if start == '1' or start == 'value proposition':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            ValueProposition1()    

        elif start == '2' or start == 'customer segment':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            customersegment() 

        elif start == '3':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            ChannelsofCommunication()
            
        elif start == '4':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            CustomerRelationships()

        elif start == '5':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            KeyActivities()

        elif start == '6':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            KeyResources()

        elif start == '7':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            KeyActivities()

        elif start == '8':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            CostStructure()

        elif start == '9':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
            RevenueStream()
    
        else:
            print('please choose one of the nine components of our business.')
            print()
            time.sleep(2)

#components will return to here
def Mainintersection():
    #import modules
    import time
    import random
    import sys

    while True:
            print(hisname + ' which one of the nine components do you want to go to next?')
            print("(input it's number")
            print(hisname + ' if you are done with all of them input END )')
            print('  1-Value Proposition')
            print('  2-Customer Segment(s)')
            print('  3-Channels of Communication')
            print('  4-Customer Relationships ')
            print('  5-Key Activities')
            print('  6-Key Resources')
            print('  7-Key Partners')
            print('  8-Cost Structure')
            print('  9-Revenue Stream')
            start = input()

            if start == '1' or start == 'value proposition':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                ValueProposition1()    

            elif start == '2' or start == 'customer segment':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                customersegment() 

            elif start == '3':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                ChannelsofCommunication()
                
            elif start == '4':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                CustomerRelationships()

            elif start == '5':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                KeyActivities()

            elif start == '6':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                KeyResources()

            elif start == '7':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                KeyPartners()

            elif start == '8':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                CostStructure()

            elif start == '9':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                RevenueStream()

            elif start == 'end' or start == 'END':
                print('going to conclusion')
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                end()    
                
            else:
                print('please the number of one of the nine components of our business.')
                print('(or input END if you are done)')
                print()
                time.sleep(2)

#ending will come to here
def Mainintersection3():
    while True:
            print(hisname + ' which one of the nine components did you miss?')
            print('  1-Value Proposition')
            print('  2-Customer Segment(s)')
            print('  3-Channels of Communication')
            print('  4-Customer Relationships ')
            print('  5-Key Activities')
            print('  6-Key Resources')
            print('  7-Key Partners')
            print('  8-Cost Structure')
            print('  9-Revenue Stream')
            start = input()

            if start == '1' or start == 'value proposition':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                ValueProposition1()    

            elif start == '2' or start == 'customer segment':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                customersegment() 

            elif start == '3':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                ChannelsofCommunication()
                
            elif start == '4':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                CustomerRelationships()

            elif start == '5':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                KeyActivities()

            elif start == '6':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                KeyResources()

            elif start == '7':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                KeyPartners()

            elif start == '8':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                CostStructure()

            elif start == '9':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                RevenueStream()

            elif start == 'end' or start == 'END':
                print('please wait...')
                for d in range(3):
                    print(str(3 - d))
                    time.sleep(1)
                end()    
                
            else:
                print('please choose one of the nine components of our business.')
                print()
                time.sleep(2)
                
#the 9 components DEF
                
#the first component            
def ValueProposition1():
    print('Value Propositions')
    print()
    time.sleep(1)
    
    print('our Value Propositions is divided into:')
    time.sleep(1)
    print()
    
    print('  1-Value Offered')
    print()
    
    print('  2-Customers Needs')
    print()
    
    print('  3-Problem Solved')
    print()
    
    print('  4-Bundle Benefits')
    time.sleep(2)
    print()
    
    print(hisname + ' do you think that we should add to or change in our Value Propositions?')
    print('(please state how)')
    comment1 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    while True:
        print(hisname + ' which one of our Value Propositions do you want to know about first?(input the number)')
        print('  1-Value Offered')
        print()
    
        print('  2-Customers Needs')
        print()
    
        print('  3-Problem Solved')
        print()
    
        print('  4-Bundle Benefits')        
        VP = input()
        print()

        if VP == '1':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ValueOffered()
            
        elif VP == '2':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            CustomersNeeds()

        elif VP == '3':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ProblemSolved()

        elif VP == '4':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            BundleBenefits()

        else:
            print(hisname + ' please choose one of the four Value Propositions')
            print()
            time.sleep(2)
            
#the non-comment asking VP
def ValueProposition():
    print()
    
    while True:
        print('Value Propositions')
        print()
        time.sleep(1)
        
        print(hisname + ' which one of our Value Propositions do you want to know about next?(input the number)')
        print('  1-Value Offered')
        print()
    
        print('  2-Customers Needs')
        print()
    
        print('  3-Problem Solved')
        print()
    
        print('  4-Bundle Benefits')        
        VP = input()

        if VP == '1':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ValueOffered()
            
        elif VP == '2':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            CustomersNeeds()

        elif VP == '3':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ProblemSolved()

        elif VP == '4':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            BundleBenefits()

        else:
            print('please check the spelling')
            print()
            time.sleep(2)
            
#DEF of VP
def ValueOffered():
    print('Value Offered')
    print()
    time.sleep(1)
    
    print('Since robots are not buyable products, ')
    print('having a company that sells them will provides insane value for customers')
    time.sleep(3)
    print()
    
    print(hisname + ' do have any way for us to improve our Value Offered?')
    print('(please state how)')
    comment2 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    while True:
        print(hisname + ' are you done with our Value Propositions')
        VS = input()

        if VS == 'n' or VS == 'no':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ValueProposition()

        elif VS == 'y' or VS == 'yes':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        else:
            print('please input yes or no')
            time.sleep(2)
            
def CustomersNeeds():
    print('Customers Needs')
    print()
    time.sleep(1)
    
    print('With the new idea of robots we are going to make people realize a need they didn’t now (newness). ')
    print('As robots will help improve people’s lives.')
    print()
    
    print(hisname + ' do have any way for us to improve our Customers Needs?')
    print('(please state how)')
    comment3 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    newQ()
    
#part of the Customers Needs    
def newQ():
    while True:
        print('do you know what is our newness?(lowercase yes or no)')
        new = input()
        
        if new == 'no' or new == 'n':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            newness()

        elif new == 'y' or new == 'yes':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            CNNend()

        else:
            print('please input yes of or no')
            time.sleep(2)
            
            
def newness():
    print('newness')
    print()
    time.sleep(1)

    print('what is newness?')
    time.sleep(1)
    print('new|ness is the quality of being new or original')
    print()

    print('as for our newness')
    print('We are creating a new world where robots will help humans develop and progress ')
    print()
    
    print(hisname + ' do have any way for us to improve our newness?')
    print('(please state how)')
    comment4 = input()
    print('thank you ' + hisname + ' for the feedback.')
    
    print('please wait...')
    for d in range(3):
            print(str(3 - d))
            time.sleep(1)
    CNNend()

def CNNend():
    print(hisname + ' are you done with our Value Propositions?')
    print('  1-Value Offered')
    print()
    
    print('  2-Customers Needs')
    print()

    print('  3-Problem Solved')
    print()
    
    print('  4-Bundle Benefits')
    op = input()

    if op == 'y' or op == 'yes':
        print('please wait...')
        for d in range(3):
            print(str(3 - d))
            time.sleep(1)
        Mainintersection()

    elif op == 'n' or op == 'no':
        print('please wait...')
        for d in range(3):
            print(str(3 - d))
            time.sleep(1)
        ValueProposition()

    else:
        print('please choose yes or no')
        time.sleep(2)
        
def ProblemSolved():
    print('Problem Solved')
    print()
    time.sleep(1)
    
    print("Robots will provide help in our customer's daily life.")
    print('the help that the robot can provide is insanly uncountable.')
    print()
    
    print(hisname + ' do have any way for us to improve our Problem Solved?')
    print('(please state how)')
    comment5 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()

    while True:
        print('Are you done with our Value Proposition?')
        op = input()

        if op == 'y' or op == 'yes':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        elif op == 'n' or op == 'no':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ValueProposition()
        else:
            print('please choose yes or no')
            time.sleep(2)
            

        
def BundleBenefits():
    print('Bundle Benefits')
    print()
    time.sleep(1)
    
    print("Our robot's design would include as much bundle usage as possible.")
    print('This is because we want our customer to get as much benefits as possible.')
    print()

    print(hisname + ' do you think that we should change in our Bundle Benefits?')
    print('(please state how)')
    comment6 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    print('please wait...')
    for d in range(3):
        print(str(3 - d))
        time.sleep(1)
    Customization()

#part of the Bundle Benefits     
def Customization():
    print('Customization')
    print()
    time.sleep(1)

    print('what is Customization?')
    time.sleep(1)
    print('cus¦tom|iza¦tion is the action of modifying something to suit a particular individual or task')
    print('a modification made to something to suit a particular individual or task')
    print('')
    time.sleep(3)
    
    print('as for our Customization')
    print('we are also going to make the customer')
    print('Customiz his own robot(Customization)')

    print(hisname + ' what do you think of our Customization?')
    print('(how do we improve it?)')
    comment7 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()

    print('please wait...')
    for d in range(3):
        print(str(3 - d))
        time.sleep(1)
    BundleBenefitsend()
    
#part of the Bundle Benefits
def BundleBenefitsend():
    print()
    while True:
        print('Are you done with our Value Propositions?')
        print('  1-Value Offered')
        print()
    
        print('  2-Customers Needs')
        print()

        print('  3-Problem Solved')
        print()
    
        print('  4-Bundle Benefits')
        op = input()

        if op == 'y' or op == 'yes':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        elif op == 'n' or op == 'no':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ValueProposition()

        else:
            print('please in put yes or no')
            time.sleep(2)
        
#the second component
def customersegment():
    print('customer segment(s)')
    print()
    time.sleep(1)
    
    print(hisname + ' here are the four customer segment(s) any company would have')
    print()
    
    print('  i.	Mass market:')
    print('     no distinguishing between customer segments')
    print()

    print(' ii. Niche market:')
    print('     very specific and specialized segments')
    print()

    print('iii. Segmented:')
    print('     slight variations between customer segments')
    print()

    print(' iv. Diversified:')
    print('     serves unrelated segments')
    print()
    time.sleep(3)
    
    print('for our company we chose both Niche and Mass marketing ')
    print('Since we are producing robots for several different uses we will use  ')
    print('mass market, still we will niche marke by making the customer design his own robot.')
    print()
    
    print(hisname + ' do you think that we should change in our customer segment(s)?')
    print('(please state how)')
    comment8 = input()
    print('thank you ' + hisname + ' for the feedback.')
    time.sleep(1)
    
    print(hisname + ' that was all fo our customer segment(s)')
    
    print('please wait...')
    for d in range(3):
        print(str(3 - d))
        time.sleep(1)
    Mainintersection()

#the third component
def ChannelsofCommunication():
    print('Channels of Communication')
    print()
    time.sleep(1)
    
    print(hisname  + ' here are our five Channels of Communication')
    print()

    print('  a.	Awareness:')
    print('     How do we raise awareness about our company’s products and services?')
    print()

    print('  b.	Evaluation:')
    print('     How do we help customers evaluate our organization’s Value Proposition?')
    print()

    print('  c.	Purchase:')
    print('     How do we allow customers to purchase specific products and services?')
    print()

    print('  d.	Delivery:')
    print('     How do we deliver a Value Proposition to customers?')
    print()
    
    print('  e.	After sales: ')
    print('     How do we provide post-purchase customer support?')

    while True:
        print('which one of our Channels of Communication')
        print('do you want to know about first?')
        print('(input the lowercase letter of the Channel)')
        Channels = input()

        if Channels == 'a':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Awareness()

        elif Channels == 'b':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Evaluation()    

        elif Channels == 'c':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Purchase()

        elif Channels == 'd':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Delivery()

        elif Channels == 'e':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Aftersales()
            
        else:
            print('please input the lowercase letter of the Channel')
            time.sleep(2)

def ChannelsofCommunication2():
    print('Channels of Communication')
    print()
    time.sleep(1)
    
    while True:
        print(hisname + 'which one of our Channels of Communication')
        print('do you want to know about next?')
        print('  a.	Awareness:')
        print('     How do we raise awareness about our company’s products and services?')
        print()

        print('  b.	Evaluation:')
        print('     How do we help customers evaluate our organization’s Value Proposition?')
        print()

        print('  c.	Purchase:')
        print('     How do we allow customers to purchase specific products and services?')
        print()

        print('  d.	Delivery:')
        print('     How do we deliver a Value Proposition to customers?')
        print()
    
        print('  e.	After sales: ')
        print('     How do we provide post-purchase customer support?')
        print('(input the lowercase letter of the Channels)')
        Channels = input()

        if Channels == 'a':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Awareness()

        elif Channels == 'b':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Evaluation()    

        elif Channels == 'c':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Purchase()

        elif Channels == 'd':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Delivery()

        elif Channels == 'e':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Aftersales()

        else:
            print('please input the lowercase letter of the Channel')
            time.sleep(2)
            
#def of the Channels          
def Awareness():
    print('Awareness')
    print('')
    time.sleep(1)

    print('what is Awareness?')
    time.sleep(1)
    print('aware|ness is knowledge or perception of a situation or fact')
    print('concern about and well-informed interest in a particular situation or development')
    print('synonyms: consciousness · recognition · realization · cognizance')

    print('press ENTER to continue')
    con = input()

    print('as for our Awareness')
    print('through our robots and online web sites ')
    print('we will make sure that our customer remain up to date.')
    print()
    time.sleep(2)
    
    print(hisname + ' what do you think of our Awareness?')
    print('(how do we improve it)')
    comment9 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    while True:
        print(hisname + ' are you done with our Channels?')
        Channel = input()

        if Channel == 'no' or Channel == 'n':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ChannelsofCommunication2()

        elif Channel == 'yes' or Channel == 'y':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        else:
            print('please input yes or no')
            time.sleep(2)
                        
def Evaluation():
    print('Evaluation')
    print()
    time.sleep(1)

    print('what is Evaluation?')
    print('evalu|ation is the making of a judgement about the amount, number, or value of something; assessment')

    print('press ENTER to continue')
    con = input()
    
    print('as for our Evaluation')
    print('by giving the customer(s) different designs of other users. ')
    print('We are making sure that he will evaluate to the best.')
    print(hisname + '  do you think we should add to')
    print('our ideas of Evaluation?(please state how)')
    comment10 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    while True:
        print(hisname + ' are you done with our Channels?')
        Channel = input()

        if Channel == 'no' or Channel == 'n':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ChannelsofCommunication2()

        elif Channel == 'yes' or Channel == 'y':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        else:
            print('please input yes or no')
            time.sleep(2)
            
def Purchase():
    print('Purchase')
    print()
    time.sleep(1)
    
    print('through our web site a customer can easily Purchase  and get gift cards')
    print()

    print('press ENTER to continue')
    con = input()
    
    print(hisname + '  do you think we should add to')
    print('our ways of Purchase?(please state how)')
    comment11 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    while True:
        print(hisname + ' are you done with our Channels?')
        Channel = input()

        if Channel == 'no' or Channel == 'n':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ChannelsofCommunication2()

        elif Channel == 'yes' or Channel == 'y':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        else:
            print('please input yes or no')
            time.sleep(2)

def Delivery():
    print('Delivery')
    print()
    time.sleep(1)
    
    print('we are going to ship the item to your home and show the shipping and delivery progress online')
    print()

    print('press ENTER to continue')
    con = input()
    
    print(hisname + '  do you think we should add to')
    print('our way of Delivery?(please state how)')
    comment12 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    while True:
        print(hisname + ' are you done with our Channels?')
        Channel = input()

        if Channel == 'no' or Channel == 'n':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ChannelsofCommunication2()

        elif Channel == 'yes' or Channel == 'y':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        else:
            print('please input yes or no')
            time.sleep(2)

def Aftersales():
    print('After sales')
    print()
    time.sleep(1)
    
    print('through out the first week our company will check if the item is doing fine.')
    print()

    print('press ENTER to continue')
    con = input()
    
    print(hisname + '  do you think we should add to')
    print('our ways of checking in the After sales?(please state how)')
    comment13 = input()
    print('thank you ' + hisname + ' for the feedback.')
    print()
    
    while True:
        print(hisname + ' are you done with our Channels?')
        Channel = input()

        if Channel == 'no' or Channel == 'n':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            ChannelsofCommunication2()

        elif Channel == 'yes' or Channel == 'y':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()
            
        else:
           print('please input yes or no')
           time.sleep(2)
           
#the fourth component
def CustomerRelationships():
    print('Customer Relationships')
    print()
    time.sleep(1)
    
    print(hisname + ' here are the main 4 Customer Relationships')
    print('  i.	Personal assistance: ')
    print('     person-to-person communication with a real person (point of sale, call center, email, etc.)')
    print()
    
    print(' ii.	Self-service: ')
    print('     No direct relationship with customers')
    print()
    
    print('iii.	Communities:')
    print('     connections between the company and a group of customers, and connections between community members only')
    print()

    print('iv.	Co-creation:')
    print('     collaborating with customers to create value')
    print('')
    time.sleep(3)

    print('which one of our 4 Customer Relationships')
    print('do you think suits us the most and why?')
    comment14 = input()
    print('thank you ' + hisname + ' for the feedback.')
    
    while True:
        print('')
        print(hisname + ', for each one of the 4 Customer Relationships')
        print('we clarified how we are going to')
        print('(1)Build(create),(2)implement, and(3)sustain them.')
        print('we also have clarified why is it good for us')
        print()
        
        time.sleep(2)
        print('which one of them do you want to know about first?')
        print('please state its number(1, 2, 3,or 4)')
        CR = input()

        if CR == "1":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Personalassistance()

        elif CR == "2":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Selfservice()

        elif CR == "3":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Communities()

        elif CR == "4":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Cocreation()

        else:
            print('please choose input the number of the Customer Relationships')
            time.sleep(2)

#the defs of Customer Relationships
def CustomerRelationshipstransport2():
    print('Customer Relationships')
    print()
    time.sleep(1)
    
    print(hisname + ' here are our 4 Customer Relationships')
    time.sleep(1)
    print('  i.	Personal assistance: ')
    print('     person-to-person communication with a real person (point of sale, call center, email, etc.)')
    print()
    
    print(' ii.	Self-service: ')
    print('     No direct relationship with customers')
    print()
    
    print('iii.	Communities:')
    print('     connections between the company and a group of customers, and connections between community members only')
    print()

    print('iv.	Co-creation:')
    print('     collaborating with customers to create value')
    print('')
    
    while True:
        print()
        print('which one of them do you want to know about next?')
        print('please state its number(1, 2, 3,or 4)')
        CR = input()

        if CR == "1":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Personalassistance()

        elif CR == "2":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Selfservice()

        elif CR == "3":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Communities()

        elif CR == "4":
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Cocreation()

        else:
            print('please choose one of our 4 Customer Relationships')
            time.sleep(2)
    
def CustomerRelationshipstransport():
    while True:
        print()
        print(hisname + ' are you done with our Customer Relationships?')
        rt = input()

        if rt == 'y' or rt == 'yes':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Mainintersection()

        if rt == 'n' or rt == 'no':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            CustomerRelationshipstransport2()
        else:
            print('please input yes or no')
            time.sleep(2)
            
#1
def Personalassistance():
    print('Personal assistance')
    print()
    time.sleep(1)
    
    print('1.why it is good for us ')
    print('it would useful to us if there was a network problem')
    print()
    time.sleep(2)
    
    print('2.we are going to Build(create) it through')
    print('creating a 24/7 Personal assistance support.')
    print()
    time.sleep(2)
    
    print('3.we are going to implement it through')
    print('creating a customer center where customers can get Personal assistance.')
    print()
    time.sleep(2)
    
    print('4.we are going to sustain it through')
    print('getting comments from each customer in the customer center.')
    print()
    time.sleep(2)
    
    print(hisname + ' what do you think of our')
    print('Personal assistance?')
    comment15 = input()
    print('thank you ' + hisname + ' for the feedback.')
    
    CustomerRelationshipstransport()
    
#2    
def Selfservice():
    print('Self-service')
    print()
    time.sleep(1)
    
    print('1.why it is good for us ')
    print('it would be useful to us because it is an indirect way to show our coding abilities')
    print()
    time.sleep(2)
    
    print('2.we are going to Build(create) it through')
    print('creating an Online web-sites, and programmed robots.')
    print()
    time.sleep(2)
    
    print('3.we are going to implement it through')
    print('creating the codes for both the Online web-sites, and the programmed robots.')
    print()
    time.sleep(2)
    
    print('4.we are going to sustain it through')
    print('enhancing our robots update our web-sites to meet the needs of the customer.')
    print()
    time.sleep(2)
    
    print(hisname + ' what do you think of our')
    print('Self-service?')
    comment16 = input()
    print('thank you ' + hisname + ' for the feedback.')
    
    CustomerRelationshipstransport()
    
#3
def Communities():
    print('Communities')
    print()
    time.sleep(1)
    
    print('1.why it is good for us ')
    print('it would be useful to us because it will provide ways for us to improve')
    print()
    time.sleep(2)
    
    print('2.we are going to Build(create) it through')
    print('creating Both communities that we are involved in and not involved in will be created.')
    print()
    time.sleep(2)
    
    print('3.we are going to implement it through')
    print('creating a special web-site for our community.')
    print()
    time.sleep(2)
    
    print('4.we are going to sustain it through')
    print('making our community involve asking the customers to rate this community, and ways to sustain it.')
    print()
    time.sleep(2)
    
    print(hisname + ' what do you think of our')
    print('Communities?')
    comment17 = input()
    print('thank you ' + hisname + ' for the feedback.')

    CustomerRelationshipstransport()
#4
def Cocreation():
    print('Co-creation')
    print()
    time.sleep(1)
    
    print('1.why it is good for us ')
    print('it would be useful to us because it will guarantee us more understanding of our customers')
    print()
    time.sleep(2)
    
    print('1.we are going to Build(create) it through')
    print('Asking customer  for comments to see whether or not they can benefit us ')
    print()
    time.sleep(2)
    
    print('2.we are going to implement it through')
    print('creating a co-creation center were both the customers we choose or think they can benefit us will present their ideas')
    print()
    time.sleep(2)
    
    print('3.we are going to sustain it through')
    print('making The main question in our co-creation center how to sustain this center')
    print()
    time.sleep(2)
    
    print(hisname + ' what do you think of our')
    print('Co-creation?')
    comment18 = input()
    print('thank you ' + hisname + ' for the feedback.')
    
    CustomerRelationshipstransport()
    
#the fivth component
def KeyActivities():
    print('Key Activities')
    print()
    time.sleep(1)
    
    print('A main key activity for us is improvement for all of the following: Value Proposition,  channels of Communication , production, and relationship. ')
    print(' Also we are doing our best to strength the customer relationship  through continuously checking on them before and after receiving our product(s)')
    print()
    time.sleep(3)
    
    print('for our Key Activities we have both')
    print()
    time.sleep(1)
    
    print(' 1.	Start-up activities') 
    print('  i.Production – related to designing, making, and delivering a product/service in substantial quantities or of superior quality')
    print(' ii.Problem solving – creating new solutions to individual customer problems')
    print('iii.	Platform/network – continuous development, maintenance, and enhancement of a platform or network')
    print()
          
    print(' 2.  Ongoing activities')
    print(' i.Production – related to designing, making, and delivering a product/service in substantial quantities or of superior quality')
    print('ii.Problem solving – creating new solutions to individual customer problems')
    print('iii.Platform/network – continuous development, maintenance, and enhancement of a platform or network')
    print()

    while True:
        print(hisname + ' which one do you want to know about first?(1(Start-up activities) ,or 2(Ongoing activities))')
        ka = input()

        if ka == '1':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Startupactivities()

        elif ka == '2':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)
            Ongoingactivities()

        else:
          print('please choose 1 ,or 2')
          time.sleep(2)
          print()          

#def of Key Activities           
def Startupactivities():
    #import modules
    import time
    import random
    import sys
    
    print('Start-up activities')
    print()
    time.sleep(1)
      
    print('  i.Production – we are going to let the customer design his robot,')
    print(' then we will produce the robot he designed.')
    print()
    time.sleep(1)

    print(' ii.Problem solving – to create new solutions to individual customer problems ')
    print('we will have a comment box to let the customer express the problems or solutions.')
    print(' Also we are going to check on the product one week after the customer has received his product.')
    print()
    time.sleep(2)
      
    print("iii.Platform/network – we will achieve continuous development, maintenance, and enhancement of a platform and network")
    print('from comments that we will gain from our customers.')
    print()
    time.slep(1)

    print(hisname + ' do you think we shuld add to or change in our')
    print('Start-up activities?(please state how)')
    comment18 = input()
    print('thank you ' + hisname + ' for the feedback.')

    while True:
        print('did you check our Ongoing activities?')
        af = input()

        if af == 'y' or af == 'yes':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)   
            Ongoingactivities()

        elif af == 'n' or af == 'no':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)   
            Mainintersection()

        else:
            print('please input yes or no')
            time.sleep(2)
      

            
def Ongoingactivities():
      print('Ongoing activities')
      print()
      time.sleep(1)
      
      print('  i.Production – we will keep improving our production speed and style.')
      print(' Also we will create new styles of producing our robots.')
      time.sleep(1)
      print()

      print(' ii.Problem solving – we will solve the problems of (1) our customers, (2)having to be up to date, and (3)other company issues.')
      print()
      time.sleep(1)

      print('iii.Platform/network – we will develop ')
      print('and try new styles of networks and test the customer’s reactions ')
      print('to achieve continuous development, maintenance, and enhancement of a platform and network.')
      time.sleep(1)

      print(hisname + ' do you think we shuld add to or change in our')
      print('Ongoing activities?(please state how)')
      comment19 = input()
      print('thank you ' + hisname + ' for the feedback.')

      while True:
          print('did you check our Start-up activities?')
          af = input()

          if af == 'y' or af == 'yes':
              print('please wait...')
              for d in range(3):
                  print(str(3 - d))
                  time.sleep(1)   
              Startupactivities()

          elif af == 'n' or af == 'no':
              print('please wait...')
              for d in range(3):
                  print(str(3 - d))
                  time.sleep(1)   
              Mainintersection()

          else:
              print('please input yes or no')
              time.sleep(2)

#the sixth component
def KeyResources():
    print('Key Resources')
    print()
    time.sleep(1)

    print(hisname + ' here are our 4 main Key Resources:')
    print(' a. Physical – buildings, computers, vehicles')
    print(' b. Financial – stocks, bonds, cash')
    print(' c. Intellectual – ideas, patents')
    print(' d. Human - employees')
    print()
    time.sleep(1)

    print(hisname + ' here is a basic summary for our Key Resources')
    print()
    
    print('We need to have physical, and financial resources to be able to produce our unique robots.')
    print('Also, since we are doing a new idea we need to improve it, and to do so we need a lot of intellectual resources.')
    print('We need a lot of human resources which could be just an employ,a partner, or a creative person to provide us with ideas.')
    time.sleep(3)

    print(hisname + ' what do yoou think of our ')
    print('Key Resources?(how do we improve it?)')
    comment20 = input()
    print('thank you ' + hisname + ' for the feedback.')

    print('press ENTER to continue')
    con = input()

    print('returning to the nine components')
    print('please wait...')
    for d in range(3):
        print(str(3 - d))
        time.sleep(1)   
    Mainintersection()
    
#the seventh component    
def KeyPartners():
    print('Key Partners')
    print()
    time.sleep(1)

    print(hisname + ' here is the main types of partners a busniess can have:')
    print('   a. alliance between non-competitors - Joining with other businesses which are not competitors')
    print('   b. Partnering with a competitor - usually to win againest another common competitor')
    print('   c. Working with another company to start a new business - to he hlep create a big start')
    print('   d. Partnering with buyers and/or suppliers - to assure reliable supplies')
    time.sleep(3)
    print()

    print('The relationship with our partner(if any) would be an alliance between non-competitors.')
    time.sleep(1)
    print(' This is because Our company believes that joining forces with a company that has a different profusion will be very useful to us.')
    print('Because we want to make sure we provide the highest levels of bundle benefits(part of Value Proposition) and the highest levels of improvements.')
    print('The main reason other companies would be interested in joining forces with is ')
    print('that we are providing a new idea to change the world (robotics) that will easily. This idea will give them a huge advantage and reputation.')
    time.sleep(3)

    print(hisname + ' what do yoou think of our ')
    print('Key Partners?(how do we improve it?)')
    comment21 = input()
    print('thank you ' + hisname + ' for the feedback.')

    print('press ENTER to continue')
    con = input()

    print('returning to the nine components')
    print('please wait...')
    for d in range(3):
        print(str(3 - d))
        time.sleep(1)   
    Mainintersection()
    

#the eightth component
def CostStructure():
    print('Cost Structure')
    print()
    time.sleep(1)

    print(hisname + ' in this part of the program you get to know ')
    print('(1)our largest cost, (2)our most important cost, (3)what is the structure of our busniess, ')
    print('(4)three fixed costs, and(5)three variable costs')
    print()
    time.sleep(2)

    print('(1)our largest cost is the material we need to build the robots.')
    print()
    
    print('press ENTER to continue')
    con = input()

    print("(2)our most important cost is the robot's program we install in our robots.")
    print()
    
    print('press ENTER to continue')
    con = input()
    
    print('(3)our busniess structure would be a value-driven structure, because when it comes to robots value is more important.')
    print()
    
    print('what is a value-driven structure?')
    print('value-driven companies focus on giving value')
    print()
    
    
    print('press ENTER to continue')
    con = input()
    #answer
    print()

    print('(4)three of our fixed costs would be')
    print('   a. the cost that my partner will gain.')
    print('   b. the cost for each type of robotos.')
    print('   c. the Revenue that the invester would')
    print()
    
    print('press ENTER to continue')
    con = input()

    print('(5)three of our variable costs would be ')
    print('   a. the additional programs that we create by order. ')
    print('   b. the salary for the founder of new ideas for our company.')
    print("   c. any addtions to the customer's robot")
    print()
    
    print('press ENTER to continue')
    con = input()

    print(hisname + ' what do yoou think of our ')
    print('five Cost Structures?(how do we improve them?)')
    comment22 = input()
    print('thank you ' + hisname + ' for the feedback.')
    
    print('returning to the nine components')
    print('please wait...')
    for d in range(3):
        print(str(3 - d))
        time.sleep(1)   
    Mainintersection()

    


#the ninth component    
def RevenueStream():
    print('Revenue Stream(s)')
    print()
    time.sleep(1)

    print('what is a Revenue?')
    time.sleep(2)
    print('For a company, a Revenue is the total amount of money received by the company for ')
    print('goods sold or services provided during a certain time period.')
    print()
    
    print('press ENTER to continue')
    con = input()

    print(hisname + ' here are the two main types of Revenue Stream(s)')
    time.sleep(1)
    print('')

    print('One-time Revenues:')
    print(' also known as transactional revenues, where the customer pays just once for the value.')
    print()
    
    print('Recurring Revenues:')
    print(' where the customer pays over and over to continue receiving the value, ')
    print('or they pay over and over to receive ongoing support for their initial purchase.')
    print()
    
    print('press ENTER to continue')
    con = input()

    print('our company follows recurring revenue, as we are making sure for the customer to get our new robots')
    print('by notifying them of the new robots that are being produced.')
    print('we will notifying them through the communities that we made(Channels),  ')
    print('and also through our websites and the robots that they bought.')
    print()
    
    print('press ENTER to continue')
    con = input()

    print('So one-time payments and recurring payments are the broad methods by which an organization can generate revenues, ')
    print('but here are some specific methods of generating revenues which fall within these two categories…')
    print()
    
    print('   i. Asset Sale:')
    print('      selling ownership rights to a physical product')
    print()

    print('  ii. Usage Fee:')
    print('      revenue generated by use of a service (the more a customer uses the more the customer pays')
    print()

    print(' iii. Subscription Fee:')
    print('      generated by selling continuous access to a service')
    print()

    print('  iv. Advertising:')
    print('      revenue from fees for advertising a brand, product, or servicei. Asset Sale: selling ownership rights to a physical product')
    print()
    
    print('press ENTER to continue')
    con = input()

    print('because our main product is robot(s), ')
    print('we believe that the method that we will use the most is ')
    time.sleep(1)
    print()
    
    print('   i. Asset Sale:')
    print('      selling ownership rights to a physical product')
    time.sleep(1)
    print()
          
    print('this is because our customers would obiviously want')
    print('the ownership of the robot.')
    print()
          
    print('press ENTER to continue')
    con = input()

    print(hisname + ' what do yoou think of our ')
    print('Revenue Stream(s)?(how do we improve them?)')
    comment23 = input()
    print('thank you ' + hisname + ' for the feedback.')

    print('returning to the nine components')
    print('please wait...')
    for d in range(3):
        print(str(3 - d))
        time.sleep(1)   
    Mainintersection()

#the ending of the program
def end():
    print(hisname + ' you have reached the conclusion(ending) of the FBP(the Full Business Program)')
    time.sleep(1)

    while True:
        print('are you perfectly sure that you are done with the nine components?')
        print(' 1-Value Proposition')
        print(' 2-Customer Segment(s)')
        print(' 3-Channels of Communication')
        print(' 4-Customer Relationships ')
        print(' 5-Key Activities')
        print(' 6-Key Resources')
        print(' 7-Key Partners')
        print(' 8-Cost Structure')
        print(' 9-Revenue Stream')
        done = input()

        if done == 'y' or done == 'yes':
            print()
            end2()
            
        elif done == 'n' or done == 'no':
            print('please wait...')
            for d in range(3):
                print(str(3 - d))
                time.sleep(1)   
            Mainintersection3()

        else:
            print(hisname + ' please input yes or no')
            print()
            time.sleep(2)

#the real ending
def end2():
    print('do you have any last feedback to tell us')
    comment24 = input()
    print('thank you ' + hisname + ' for your last feedback.')
    print('and thank you ' + hisname + ' for using our FBP(the Full Business Program)')
    print()
    
    print('we hope that this program was usful to you')
    print('as much as it will be for us')
    print()
    time.sleep(2)

    print('thank you for everything and have a nice day ' + hisname)
    print()

    print('press ENTER to END')
    con = input()
    sys.exit()
        
#the start of the pogram:-

Basicintroduction()

#the program gets the customer's name
print('')
print('Hello world!!')
print('welcome to the FBP(the Full Business Program)')
print('kindly enter your name')
hisname = input()

introduction()
        









