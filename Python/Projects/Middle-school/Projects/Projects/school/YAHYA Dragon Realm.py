import random
import time

def displayintroduction():
    print('you are in a land filled with dragons')
    print('you find two caves')
    print('in the first cave, the dragon is friendly, and')
    print('he is willing to share his trease with you.')
    print('the other cave is having a greedy and a hungry dragon')
    print('who will eat you on sight.')

def chooseCave():
    cave=''
    while cave != '1' and cave != '2':
        print('which cave will you approach?(1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('you approach the cave...')
    time.sleep(2)
    print('it is dark and spooky...')
    time.sleep(2)
    print('suddenly a humangus dragon jumps out in front of you! he opens his jaws and ...')
    print()
    time.sleep(2)

    friendlyCave = 2

    if chosenCave == str(friendlyCave):
        print('Then he gives you his treasure')
    else:
        print('Gobbles you down in one bite')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayintroduction()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
        
