
#how to do shuffle in python
example = [1,2,3,4,5,6,7]
#import the shuffle module like below
from random import shuffle
#then use shuffle function to shuffle a list
shuffle(example)# it doesnt return any thing
print(example)#[7, 3, 5, 2, 4, 6, 1]
#after each shuffle it will give different result as it is shuffling the list
shuffle(example)
print(example)#[5, 4, 2, 3, 7, 6, 1]

result =shuffle(example)# no return here as we are just shuffling the list
print(result)#Nonr
print(type(result))#<class 'NoneType'>

def shuffle_list(mylist):# this is a function for shuffling can call and use for any list
    shuffle(mylist)
    return mylist

result1 = shuffle_list(example)# this gives result because it uses a function we defined with shuffle
print(result1)#[1, 5, 3, 6, 7, 2, 4]


myList = [' ', 'O',' ']
shuffle_list(myList)
print(myList)#['O', ' ', ' ']

#to ask user to guess the number in a list we created
#it will keep asking till user choose one of the number in the list
def player_guess():
    guess =''
    while guess not in ['0','1','2']:
       guess = input('Pick a number: 0,1 or 2')
    return int(guess)

player_guess()


def check_guess(myList, guess):
    if myList[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess")
        print(myList)
#initial list
myList = [' ', 'O',' ']
##shuffle list
mixedup_list = shuffle_list(myList)
#user guess
guess = player_guess()
#check guess
check_guess(mixedup_list,guess)# this takes the result of two function here

#solution link for function part
#https://docs.google.com/document/d/181AMuP-V5VnSorl_q7p6BYd8mwXWBnsZY_sSPA8trfc/edit?usp=sharing