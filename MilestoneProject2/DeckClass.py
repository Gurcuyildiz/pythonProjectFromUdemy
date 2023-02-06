import random

import CardClass

class Deck():
    def __init__(self):
        self.all_cards = []

        for suit in CardClass.suits:
            for rank in CardClass.ranks:
                created_card = CardClass.Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)

    # this will remove one card each time executed, the all other cards is 51 not 52
    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()
#print(new_deck.all_cards)# will give all card class object location
first_card = new_deck.all_cards[0]
print(new_deck.all_cards[0])#Two of Hearts
bottom_card = new_deck.all_cards[-1]
print(bottom_card)#Ace of Clubs

new_deck.shuffle()# here I am shuffling the card so there is no order anymore, the last one will be different
print(new_deck.all_cards[-1]) #Nine of Diamonds

new_deck.shuffle()# I shuffled again
print(new_deck.all_cards[-1])#King of Hearts


my_card = new_deck.deal_one()
print(my_card)

#
# for card_object in new_deck.all_cards:
#     print(card_object)

#this for loop printed all card 4 times why
'''
Two of Hearts
Three of Hearts
Four of Hearts
Five of Hearts
Six of Hearts
Seven of Hearts
Eight of Hearts
Nine of Hearts
Ten of Hearts
Jack of Hearts
Queen of Hearts
King of Hearts
Ace of Hearts
Two of Diamonds
Three of Diamonds
Four of Diamonds
Five of Diamonds
Six of Diamonds
Seven of Diamonds
Eight of Diamonds
Nine of Diamonds
Ten of Diamonds
Jack of Diamonds
Queen of Diamonds
King of Diamonds
Ace of Diamonds
Two of Spades
Three of Spades
Four of Spades
Five of Spades
Six of Spades
Seven of Spades
Eight of Spades
Nine of Spades
Ten of Spades
Jack of Spades
Queen of Spades
King of Spades
Ace of Spades
Two of Clubs
Three of Clubs
Four of Clubs
Five of Clubs
Six of Clubs
Seven of Clubs
Eight of Clubs
Nine of Clubs
Ten of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs
Ace of Clubs



'''