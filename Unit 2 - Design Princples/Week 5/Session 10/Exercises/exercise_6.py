# Exercise 6

# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

# The Deck class should return a random single card from the cards.

import random
import itertools

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value  
        
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)
        
class Deck:
    def __init__(self):
        suits = ['Hearts','Diamonds','Clubs','Spades'] 
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        
        deck = list(itertools.product(values, suits))
        random.shuffle(deck)

        for i in range(1):
            suit_val = deck[i][0]
            value_val = deck[i][1]

            print(Card(value_val,suit_val))


deck = Deck()
print(deck)