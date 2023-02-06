
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


def gameon_choice():# bu bitti
    choice ='wrong'
    while choice not in ['Y', 'N']:
        choice = input('Would you like to keep playing? Y or N')

        if choice not in ['Y', 'N'] :
            print("Sorry, Please make sure to choose Y or N.")

    if choice == 'Y'  :
        return True
    else:
        return False

#print(gameon_choice())


def position_choice():
    choice = 'Wrong'
    while choice not in [1,2,3,4,5,6,7,8,9] :
        choice = input('Choose your next position (1-9)')
        if choice not in ['1','2','3','4','5','6','7','8','9']:
           # clear_output()
            print('Sorry invalid response! Please enter a number between (1-9) ')
    return int(choice)
#print(position_choice())


mylist = []
def replacement_choice(mylist, position):
    user_placement = input('Type X to place on the board at the position')
    mylist[position] = user_placement
    return mylist
#print(replacement_choice(mylist, 1))



#test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board1 =[' ']*10
def display_board(board ):
    print('\n'*10)
    print(board[1]+' | '+ board[2]+' | '+board[3])
    print('----')
    print(board[4]+' | '+ board[5]+' | '+board[6])
    print('----')
    print(board[7]+' | '+ board[8]+' | '+board[9])


#
def who_win(display_board, player_input):
    if display_board[1] == display_board[2] == display_board[3] or display_board[4] == display_board[5] == display_board[6] or display_board[7] == display_board[8] == display_board[9]:
        print('Congratulations! you won')


#print(display_board(test_board))
print(display_board(test_board1))

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









