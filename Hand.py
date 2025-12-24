"""
CS 1026A Fall 2025
Assignment 4: Blackjack
Created by: Sahasra Chityala
Student ID: schitya
Student Number: 251512858
File created: December 6th

this file creates the hand class which is a group of cards that a
player is holding. it must be able to add cards and calculate the hand's
total value and ace rules etc.
"""


from Card import *

class Hand:

    def __init__(self):
        #we start with an empty list since the player begins the round with no cards
        self._hand = []

    def add_card(self, card):
        # then add the given card to the hand
        self._hand.append(card)

    def total(self):
        #this method figures out the numeric total of the hand
        # face cards count as 10, number cards count as their number,
        # and then aces can count as either 1 or 11

        # sum of all non-ace cards
        total_no_ace = 0

         #this helps count how many aces there are
        ace_count = 0

        # loop through each card and compute normal values first
        for c in self._hand:
            r = c.get_rank()

            if r in ["J", "Q", "K"]:
                # face cards always count as 10 so we add 10 to non ace count
                total_no_ace += 10

            elif r == "A":
                # it is A then increment the count and store it for later
                ace_count += 1
            else:
                # numeric card (2–10)
                total_no_ace += int(r)

        # if there are no aces, then the total is just non ace count
        if ace_count == 0:
            return total_no_ace

        # if there are aces, we calculate two totals:
        # first is all aces counted as 1 each
        low_total = total_no_ace + ace_count * 1

        # second we treat exactly one ace as 11 and the others as 1
        # this gives the soft total that might help reach 21
        high_total = total_no_ace + 11 + (ace_count - 1)

        # returning a tuple gives both totals so the game decide which one to use
        return (low_total, high_total)

    def __str__(self):
        # if no cards then it should say "Empty hand"
        if len(self._hand) == 0:
            return "Empty hand"

        # make a list of each converted to a string
        card_strs = []
        for c in self._hand:
            card_strs.append(str(c))

        #then we must put them inside curly brackets
        cards_section = "{"+", ".join(card_strs)+"}"

        #this shows the calculated total values beside the cards
        return f"{cards_section}, Total: {self.total()}"