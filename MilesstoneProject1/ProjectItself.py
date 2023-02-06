'''Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python"
 otherwise you won't learn anything!)
 Keep in mind that this project can take anywhere between several hours to several days.'''

'''
Sample output
1- Welcome to Tic Tac Toe !
2- Player 1: Do you want to be X or O 
# X
3- Player 1 will go first
4- Are you ready to play? Enter Yes or No
#Y
5-Choose your next position : (1-9)
   |   |  
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
----------
   |   |
   |   |
   |   |
#when user enter 1 such as then printed board will be like this
   |   |  
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
----------
   |   |
X  |   |
   |   |
6-Choose your next position : (1-9)
#when user enter 8 as an example
   |   |  
   | O |
   |   |
-----------
   |   |
   |   |
   |   |
----------
   |   |
X  |   |
   |   |
7-Choose your next position : (1-9)
#when user enter 2 as an example
   |   |  
   | O |
   |   |
-----------
   |   |
   |   |
   |   |
----------
   |   |
X  | X |
   |   |
8-Choose your next position : (1-9)
#when user enter 9 as an example
   |   |  
   | O | O
   |   |
-----------
   |   |
   |   |
   |   |
----------
   |   |
X  | X |
   |   |
9-Choose your next position : (1-9)
#when user enter 3 as an example
   |   |  
   | O | O
   |   |
-----------
   |   |
   |   |
   |   |
----------
   |   |
X  | X | X
   |   |
Congratulations! You have won the game
10- Hey do you want to play the game again ?  Enter Y or N 
# N
11 this no answer will break the cell
#'''


'''Usefultips
'''
#1-
#print('Welcome to Tic Tac Toe !')
#2-
# Player 1 : Do you want to be X or O
# X
# Player 1 will go first
def user_choice():
    choice = 'wrong'
    while choice not in ['X', 'O']:
        player1 = input('Player 1 : Do you want to be X or O')
        if player1.capitalize() == 'X':
            print('Player 1 will go first')
            break
        elif player1.capitalize() == 'O' :
            print('Player 2 will go first')
            break
#print(user_choice())
#3-
# Are you ready to play? Enter Yes or No
# Y
def readiness():
    choice = 'wrong'
    choice =input('Are you ready to play? Enter Yes or No')
    while choice not in [ 'Y', 'N']:
        if choice.upper() == 'Y':
            break
        elif choice.upper() == 'N':
            break
        else:
            print('Sorry! In correct input. Please enter Y for yes and N for No')
            break
    return choice
#print(readiness())
#4-
# Choose your next position (1-9)
# blank board should be printed here
#test_board1 =[' ']*10
def display_board(board ):
    print('\n'*10)
    print(board[1]+' | '+ board[2]+' | '+board[3])
    print('----')
    print(board[4]+' | '+ board[5]+' | '+board[6])
    print('----')
    print(board[7]+' | '+ board[8]+' | '+board[9])
#
def position_choice():
    choice = 'Wrong'
    while choice not in [1,2,3,4,5,6,7,8,9] :
        choice = input('Choose your next position (1-9)')
        if choice not in ['1','2','3','4','5','6','7','8','9']:
           # clear_output()
            print('Sorry invalid response! Please enter a number between (1-9) ')
    return int(choice)
#print(position_choice())

# 5- Assign user input
def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 ='X'
    return (player1,player2)


# 6- Place input on the board
mylist = []
def replacement_choice(mylist, position):
    user_placement = input('Type X to place on the board at the position')
    mylist[position] = user_placement
    return mylist
#print(replacement_choice(mylist, 1))



#10-
def who_win(display_board, player_input):
    if display_board[1] == display_board[2] == display_board[3] or display_board[4] == display_board[5] == display_board[6] or display_board[7] == display_board[8] == display_board[9]:
        print('Congratulations! you won')
    else:
        print('Nobody wins')

#11
def gameon_choice():
    choice ='wrong'
    while choice not in ['Y', 'N']:
        choice = input('Would you like to keep playing? Y or N')

        if choice not in ['Y', 'N'] :
            print("Sorry, Please make sure to choose Y or N.")

    if choice == 'Y'  :
        return True
    else:
        return False




print('Welcome to Tic Tac Toe !')
game_on  = True
while game_on:
   # user_choice()
    player_input()
    readiness()
    #position_choice()
    position = position_choice()
    test_board1 = [' '] * 10
    display_board(test_board1)
    replacement_choice(mylist,)
    who_win(display_board,player_input)
    gameon_choice()
    game_on = gameon_choice()