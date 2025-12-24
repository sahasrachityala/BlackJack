"""
this file creates the deck class which basically just a list that holds
many card objects. based on how many decks the game needs, we create
52 cards per deck in a very specific order. the deck can also shuffle itself
and let us draw the top card.
"""

from Card import *
import random

class Deck:

    def __init__(self, num_decks):
        # this list will store all the card objects in one area
        self._cards = []

        # these are the ranks and suits givens
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["clubs", "diamonds", "hearts", "spades"]

        # we need to build each deck one at a time
        for _ in range(num_decks):
            for s in suits:
                for r in ranks:
                    # create a card and put it into the list
                    self._cards.append(Card(r, s))

    def shuffle(self):
        #use random.shuffle to mix the cards, just like shuffling real cards
        random.shuffle(self._cards)

    def draw_card(self):
        # drawing the top card means removing the card at index 0
        #amd if there are no cards left then we return none to show deck empty
        if len(self._cards) == 0:
            return None
        return self._cards.pop(0)
