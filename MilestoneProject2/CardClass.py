

#all those three are global
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



class Card():# we dont have to use paranthesis here as there wont be inheritance

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    #this is a string method to return rank and suit
    def __str__(self):
        return self.rank + ' of ' + self.suit

#create an instance of class
two_hearts = Card('Hearts','Two')
print(two_hearts)#Two of Hearts

#the result is string
print(two_hearts.suit)#Hearts
print(two_hearts.rank)#Two
print(two_hearts.value)# 2

#in order to do comparison, we will create a dictionary
# values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
#             'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
#
# #when I pass the string value of rank here, it will give me int
# print(values[two_hearts.rank]) #2

#for the readibilty purpose if there is a global defined dictionary, we put into very top of class
#