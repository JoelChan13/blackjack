###############################################################################

# 8         88                       88        88                       88         
# 8         88                       88        ""                       88         
# 8         88                       88                                 88         
# 8,dPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88  ,dK  
# 8P'   "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8   
# 8      d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
# 8b,  ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"YbK 
# Y"Ybd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88  ` K
#                                             ,88                                  
#                                           888P"  

###############################################################################

########################
# Blackjack House Rules
########################

# There are no jokers present in the deck
# The Ace card can either have a value of 11 or 1, based on the cards drawn
# The suits Jack, Queen, and King have a value of 10
# All cards have equal probability of being drawn throughout the games played
# The Computer is the dealer in this Blackjack game
# The Dealer will keep hitting cards until the value reaches 17
# A hand amounting to 21 is considered as Blackjack,
# If either the player or the dealer go over 21, it means they busted.
# If no player has an amount totalling 21, the closest hand to 21 wins the game

###############################################################################
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
                {"rank": "A", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "K", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "J", "value": 10},
            ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """
        a function which shuffles the cards.
        """
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Hand:
    def __init__(self, dealer=False):
        """
        a class for hand which also keeps track of the value
        """
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        """
        add a card list to the cards using the extend method
        """
        self.cards.extend(card_list)
    
    def calculate_value(self):
        """
        adds the ability to calculate the value of a hand
        """
        self.value = 0
        ace_present = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                ace_present = True
        
        if ace_present and self.value > 21:
            # if player total exceeds 21, subtract 10 if the user has an ace
            self.value -= 10

    def get_value(self):
        """
        calculate hand value before returning value
        """
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        """
        determine whether the value of the cards has blackjack
        """
        self.calculate_value()
        return self.value() == 21
    
    def display(self):
        """
        creates a method to display information about the hand 
        and hides the dealer's second card
        """ 
        print(f'''{"Dealer’s" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards \
                 and not self.is_blackjack():
                print("hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.get_value())
        print()


class Game:
    def play(self):
        """
        creates games according to how many games the user wants to play
        """
        game_number = 0
        games_to_play = 0
        """
        converts the output from the games to play to int
        """
        games_to_play = int(input("How many games do you want to play? "))

        while not games_to_play.isdigital() or int(games_to_play) <= 0:
            print("Enter a number here.")
            games_to_play = input("How many games do you want to play? ")
        
        games_to_play = int(games_to_play)

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue
            
            choice = ""
            while player_hand.get_value() < 21 \
                    and choice not in ["s", "stand"]:
                choice = input("Please select ‘Hit’ or ‘Stand’: "). lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please select 'Hit' or 'Stand': ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                """
                creates a while loop so the dealer keeps drawing cards until 
                reaching 17 and reveals the hand after
                """
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
            
            # show all dealer cards
            dealer_hand.display(show_all_dealer_cards=True)
            
            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your Hand:", player_hand_value)
            print("Dealer Hand:", dealer_hand_value)

            """
            check winner function but not in an if statement and add a third 
            argument True to indicate the game is over
            """
            self.check_winner(player_hand, dealer_hand, True)

    def check_winner(self, player_hand, dealer_hand):
        if not game_over:
            """
            method to check the winner. if player or dealer go over 21, 
            it means they lost and their opponent won. If player or dealer 
            hit 21/blackjack, it means they won. if both players hit blackjack, 
            a tie is called.
            """
            if player_hand.get.value() > 21:
                print("You went bust. Dealer Wins")
                return True
            elif dealer_hand.get.value() > 21:
                print("Dealer went bust. You Win")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both you & dealer have blackjack. TIE")
                return True
            elif player_hand.is_blackjack():
                print("You hit blackjack. You Win")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer hit blackjack. Dealer Wins")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("TIE")
            else:
                print("Dealer Wins")
            return True
        return False


g = Game
g.play