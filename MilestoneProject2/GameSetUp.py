
from MilestoneProject2.DeckClass import Deck
from MilestoneProject2.PlayerClass import Player

#GAME SET_UP
player_one = Player('One')
player_two = Player('Two')

#Create a new deck
new_deck = Deck()
#shuffle the deck by calling the shuffle method we created
new_deck.shuffle()

#now we have to split the deck between two player
#the reason why we gave 26 is it is half of the 52
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#to check how many cards player one have
print(len(player_one.all_cards)) #26
print(len(player_two.all_cards))
print(player_one.all_cards[0])

#to start the game with a loop
game_on = True
counter_num = 0
while game_on:

    counter_num += 1
    #to see how many round it taking place
    print(f'Nunmber of round is {counter_num}')
    if len(player_one.all_cards) == 0:
        print('Player one out of the game')
        print("Player two Wins!")
        game_on = False
        break# this will break the game
    if len(player_two.all_cards) == 0:
        print('Player two out of the game')
        print("Player One Wins!")
        game_on = False
        break# this will break the game

    # Otherwise, the game is still on!

     # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        #-1 means it will draw always the last card
        if player_one_cards[-1].value > player_two_cards[-1].value:
        # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

         # No Longer at "war" , time for next round
            at_war = False

         # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

          # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

         # No Longer at "war" , time for next round
            at_war = False
        #if player has equal cards, it will print war
        else:
            print('WAR!')
        # This occurs when the cards are equal.
        # We'll grab another card each and continue the current war.

        # First check to see if player has enough cards

        # Check to see if a player is out of cards:
            #we can change number 5 given here to any number we want as a condition to win or lose
            #Higher mean shorter game
            if len(player_one.all_cards) < 5:
                 print("Player One unable to play war! Game Over at War")
                 print("Player Two Wins! Player One Loses!")
                 game_on = False
                 break

            elif len(player_two.all_cards) < 5:
                  print("Player Two unable to play war! Game Over at War")
                  print("Player One Wins! Player One Loses!")
                  game_on = False
                  break
                  # Otherwise, we're still at war, so we'll add the next cards
            else:
                 for num in range(5):
                     player_one_cards.append(player_one.remove_one())
                     player_two_cards.append(player_two.remove_one())

