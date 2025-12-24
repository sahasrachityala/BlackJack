"""
CS 1026A Fall 2025
Assignment 4: Blackjack
Created by: Sahasra Chitya;a
Student ID: schitya
Student Number: 251512858
File created: December 6th


this file creates the card class. a card just stores a rank and suit,
and the class also lets us print cards out nicely and compare them.
"""

class Card:

    def __init__(self, rank, suit):
        #we save the rank and suit so the card remembers what it is
        #these values never change once the card is made
        self._rank = rank
        self._suit = suit

    def get_rank(self):
        #return the card's rank when someone asks for it
        return self._rank

    def get_suit(self):
        # return the card's suit when needed
        return self._suit

    def __str__(self):
        #this converts the card into a short string like "AS" for ace of spades.
        # we use the first letter of the suit and keep it uppercase
        return str(self._rank) + self._suit[0].upper()

    def __eq__(self, other):
        # this checks if two cards are equal
        #two cards are equal only if they have the exact same rank AND suit
        if isinstance(other, Card):
            return self._rank == other._rank and self._suit == other._suit
        return False