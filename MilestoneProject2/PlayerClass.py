

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):#if the type of new_card is equal to list type:
            self.all_cards.extend(new_cards)# we cant use append here, otherwise it will be list in list

        #if we have a single card instead a list
        else:
            self.all_cards.append(new_cards)


    def __str__(self):
        return f' Player {self.name} has {len( self.all_cards)} cards'


new_player = Player('Jose')
print(new_player.add_cards(mycard))# Player Jose has 0 cards

new_player.add_cards()

