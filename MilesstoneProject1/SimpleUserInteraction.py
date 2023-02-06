
game_list = [0,1,2]
def display_game(game_list):
    print('here is the current list')
    print(game_list)

print(display_game(game_list))
# here is the current list
# [0, 1, 2]
import clear_output
clear_output()
def position_choice():
    # This original choice value can be anything that isn't an integer
    choice = 'WRONG'
    #While the choice is not a digit, keep asking for input.
    while choice not in [0,1,2]:
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input('Pick a position to replace (0,1,2) : ')
        #Error Message Check
        if choice not in ['0', '1', '2']:
            clear_output ()
            print('Sorry but you did not choose a valid position (0,1,2)')
    #We can convert once the while loop above has confirmed we have a digit.
    return int(choice)




def replacement_choice(game_list, position):
    user_placement = input('Type a string to place at the position')
    game_list[position] = user_placement
    return game_list

print(replacement_choice(game_list,1))
#Type a string to place at the position
#test
#[0,'test',2

def gameon_choice():# this ask the user whether they want to keep playing or not
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y', 'N']:

        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")

        if choice not in ['Y', 'N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()

            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    # Optionally you can clear everything after running the function
    # clear_output()#this clear_output is something works in jupiter notebook, may not be working here

    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False
print(gameon_choice())# if in valid response is given
#Would you like to keep playing? Y or N
# wrong
#Sorry, I didn't understand. Please make sure to choose Y or N
#Would you like to keep playing? Y or N
#Y  # if here the user gives N
#True # then ere will be False and game will be over


#this part is where we put eveything in one piece to be played
game_on = True
game_list = [0,1,2]
while game_on:
    display_game(game_list)
    position = position_choice()
    game_list =replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()

# Pick a position (0,1,2):
# Here is the current list:
#[0,1,2]
#Pick a position (0,1,2):
#two
#Sorrt but you did not choose a valid position (0,1,2)
#Pick a position (0,1,2):
#1
#Type a string to place at the position
#my choice
# Here is the current list:
#[0,'my choice',2]
#Would you like to keep playing? Y or N
#Y
#Pick a position (0,1,2):
#0
#Type a string to place at the position
#test
#Here is the current list:
#['test','my choice', 2]
#Would you like to keep playing? Y or N
#N
#game ends here


