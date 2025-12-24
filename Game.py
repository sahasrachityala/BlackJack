"""
this file creates the game class, which controls the blackjack gameplay.
it manages the deck, the playey and computers hand, turns,
decision making, and also writes results to a file at the end of the game.
"""

#import from the other classes
from Deck import *
from Hand import *

class Game:

    def __init__(self, num_decks=1):
        # create a deck with the chosen number of decks and shuffle it only once
        self._deck = Deck(num_decks)
        self._deck.shuffle()

        #this makes empty hands for the player and computer
        self._player_hand = Hand()
        self._comp_hand = Hand()

        #this keeptd track whether each player is still playing this round
        self._player_active = True
        self._comp_active = True

        #this list stores a summary of each round so we can write it to a file later
        self._results = []

    def play(self):
        #this loop keeps playing rounds until the player says "no"
        while True:
            self.play_round()
            again = input("Do you want to play again? (yes/no): ")

            # if they say no then the game will end
            if again == "no":
                break

        # after finishing all rounds ask for a filename
        # and this makes sure the user to enter something ending in .txt
        filename = input("Enter filename (ending in .txt) for the game results: ")
        while not filename.endswith(".txt"):
            filename = input("Invalid. Enter filename ending in .txt: ")

        #write all stored results to the output file
        self.output_game_results(filename)

    def play_round(self):
        #reset hands so each round starts fresh with 2 cards each
        self._player_hand = Hand()
        self._comp_hand = Hand()

        # both players start as active so set it to true
        self._player_active = True
        self._comp_active = True

        # using draw_card ensures we take from the top of the deck
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())

         #print what the hands look like right after dealing
        print("Player:", self._player_hand)
        print("Computer:", self._comp_hand)

        #now we alternate turns until both players are done
        while self._player_active or self._comp_active:

            # PLAYER TURN #
            if self._player_active:
                # ask the player what they want to do
                choice = input("What do you want to do? Type 'hit' for another card or 'stand' if you are done: ")

                if choice == "hit":
                    #this gives player a new card
                    self._player_hand.add_card(self._deck.draw_card())

                    #this checks if the player busted by examining the lowest total
                    val = self._player_hand.total()
                    low_val = val if isinstance(val, int) else val[0]

                    if low_val > 21:
                        # the player is done for the round since they cant go above 21
                        self._player_active = False
                else:
                    #otherwise player chose to stand they are also not active
                    self._player_active = False

            # COMPUTER TURN #
            if self._comp_active:
                #this compute computer totals
                val = self._comp_hand.total()

                # separate low and high totals depending on if val is int or tuple
                if isinstance(val, int):
                    low = val
                    high = val
                else:
                    low, high = val

                #putput if user stands or hits based on the number
                if high == 21:
                    comp_choice = "stand"
                elif low < 17:
                    comp_choice = "hit"
                else:
                    comp_choice = "stand"


                print("Determine what computer will do (hit/stand)")
                print(comp_choice)

                if comp_choice == "hit":
                    self._comp_hand.add_card(self._deck.draw_card())

                    #this check if computer busted
                    val2 = self._comp_hand.total()
                    low2 = val2 if isinstance(val2, int) else val2[0]

                    if low2 > 21:
                        self._comp_active = False
                else:
                    self._comp_active = False

            # after both turns this cycle then we must show updated hands to the user
            print("Player:", self._player_hand)
            print("Computer:", self._comp_hand)

        #after both are inactive then the round is over
        winner, p_score, c_score = self.determine_winner()

        print("The round has ended. Winner:", winner)

        #store the results so we can write them to a file later
        self._results.append((winner, p_score, c_score))

    def determine_winner(self):
        #this is a helper function to choose the best score (low or high) that doesn't bust
        def best_value(total):
            if isinstance(total, int):
                return total
            low, high = total
            if high <= 21:
                return high
            return low

        #this calculate both scores
        p_total = best_value(self._player_hand.total())
        c_total = best_value(self._comp_hand.total())

        #check for busted hands
        p_bust = p_total > 21
        c_bust = c_total > 21

        #handle all bust situations first
        if p_bust and c_bust:
            return "Neither", -1, -1
        if p_bust:
            return "Computer", -1, c_total
        if c_bust:
            return "Player", p_total, -1

        #if nobody busted, compare scores normally
        if p_total > c_total:
            return "Player", p_total, c_total
        elif c_total > p_total:
            return "Computer", p_total, c_total
        else:
            return "Draw", p_total, c_total

    def output_game_results(self, filename):
        #write all round results to a text file in the required format
        with open(filename, "w") as f:
            round_num = 1
            for winner, p_score, c_score in self._results:

                #wite to the file
                f.write(f"Round {round_num}\n")

                #write player score or bust
                if p_score == -1:
                    f.write("Player: bust\n")
                else:
                    f.write(f"Player: {p_score}\n")

                #write computer score or bust
                if c_score == -1:
                    f.write("Computer: bust\n")
                else:
                    f.write(f"Computer: {c_score}\n")

                #finally write the winner of that round
                f.write(f"Winner: {winner}\n\n")

                #increment it so it can move onto the results of next round
                round_num += 1
