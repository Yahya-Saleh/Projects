
import time
import sys
    
#basic intro
print('Yahya Sherif presents...')
for i in range(5):
    print(str(5 - i))
    time.sleep(1)
    
#intro
print('welcome challenger(s)')
print('to the TicTacToe game also known as XO')
time.sleep(2)
print()

#rules
print('.............................')
print('the rules are simple,')
time.sleep(1)
print()

#game rules
print('each player chooses a letter X or O')
print('the X gets to start')
print('each turn both players gets to play once')
print()

print('the first player to get his letters in a row wins')
#example
print('here is an example,')
print()

print('X|2|3')
print('-+-+-')
print('4|X|6')
print('-+-+-')
print('7|8|X')
time.sleep(2)
print()

#program rules
print('the computer will inform you whose turn is it in this two players mode.')
print()

print('to choose the area that you want to place your X or O on')
print("you need to input it's number.")
print()

#example
print('Here is an example,')
print()

print('Turn for X. which space do you want to place the X on?')
print('1')
print('X|2|3')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('7|8|9')

#ready
print()
print('are you ready?')
print('press ENTER to continue')
con = input()

#the game starts
print('.....................')
print('the game starts')
print()
time.sleep(1)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + '    1|2|3')
    print('-+-+-    -+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] + '    4|5|6')
    print('-+-+-    -+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + '    7|8|9')

def end():
    for i in range(3):
        print('please wait...')
        print(str(3 -i))
        time.sleep(1)
    game()
    
def game():
    global theBoard
    theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
    
    turn = 'X'

    while True:
        printBoard(theBoard)

        #wins for X
        
        #X
        #X
        #X
        if theBoard['1'] == 'X' and theBoard['4'] == 'X' and theBoard['7'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()
                    
                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        # X
        # X
        # X
        elif theBoard['2'] == 'X' and theBoard['5'] == 'X' and theBoard['8'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        #  X
        #  X
        #  X
        elif theBoard['3'] == 'X' and theBoard['6'] == 'X' and theBoard['9'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')
                    
        #XXX
        #
        #
        elif theBoard['1'] == 'X' and theBoard['2'] == 'X' and theBoard['3'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        #
        #XXX
        #
        elif theBoard['4'] == 'X' and theBoard['5'] == 'X' and theBoard['6'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')
                    
        #
        #
        #XXX
        elif theBoard['7'] == 'X' and theBoard['8'] == 'X' and theBoard['9'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        #X
        # X
        #   X
        elif theBoard['1'] == 'X' and theBoard['5'] == 'X' and theBoard['9'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')
             
        #  X
        # X
        #X
        elif theBoard['7'] == 'X' and theBoard['5'] == 'X' and theBoard['3'] == 'X':
            print('player X wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        #wins for O
        
        #X
        #X
        #X
        if theBoard['1'] == 'O' and theBoard['4'] == 'O' and theBoard['7'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()
                    
                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        # X
        # X
        # X
        elif theBoard['2'] == 'O' and theBoard['5'] == 'O' and theBoard['8'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        #  X
        #  X
        #  X
        elif theBoard['3'] == 'O' and theBoard['6'] == 'O' and theBoard['9'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')
                    
        #XXX
        #
        #
        elif theBoard['1'] == 'O' and theBoard['2'] == 'O' and theBoard['3'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        #
        #XXX
        #
        elif theBoard['4'] == 'O' and theBoard['5'] == 'O' and theBoard['6'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')
                    
        #
        #
        #XXX
        elif theBoard['7'] == 'O' and theBoard['8'] == 'O' and theBoard['9'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')

        #X
        # X
        #   X
        elif theBoard['1'] == 'O' and theBoard['5'] == 'O' and theBoard['9'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')
             
        #  X
        # X
        #X
        elif theBoard['7'] == 'O' and theBoard['5'] == 'O' and theBoard['3'] == 'O':
            print('player O wins')

            while True:
                print('do you want to play again?')
                print('(y for yes, and n for no)')
                again = input()

                if again == 'y':
                    end()

                elif again == 'n':
                    sys.exit()

                else:
                    print('y for yes, and n for no')
                    
        else:
            if theBoard['1'] != ' ' and theBoard['2'] != ' ' and theBoard['3'] != ' ' and theBoard['4'] != ' ' and theBoard['5'] != ' ' and theBoard['6'] != ' ' and theBoard['7'] != ' ' and theBoard['8'] != ' ' and theBoard['9'] != ' ':
                print("it's a draw.")
                while True:
                    print('do you want to play again?')
                    print('(y for yes, and n for no)')
                    again = input()

                    if again == 'y':
                        end()

                    elif again == 'n':
                        sys.exit()

                    else:
                        print('y for yes, and n for no')
                        
            else:
                print('Turn for ' + turn + '. which space do you want to place the ' + turn + ' on?')
                move = input()
                try:
                    if theBoard[move] == 'X' or theBoard[move] == 'O':
                        print(move + ' is already used choose another space')

                    elif theBoard[move] != 'X' and theBoard[move] != 'O':
                        theBoard[move] = turn

                        if turn == 'X':
                            turn = 'O'
                    
                        else:
                            turn = 'X'
                            
                except KeyError:
                    print("this place doesn't exist choose a number that is on the board")

#the start of the game
game()
