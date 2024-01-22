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
#                                          888P"  

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


class Deck:
    # a class to group the deck
    cards = []
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
            cards.append([suit, rank])
    random.shuffle(cards)

    def shuffle():
        """
        a function which shuffles the cards.
        """
        random.shuffle(cards)

    def deal(number):
        """
        function which accepts an argument to deal more than one card and return a
        list of cards instead of a single card, together with a for loop that will
        add a card from the deck for each card that was dealt.
        """
        cards_dealt = []
        for x in range(number):
            card = cards.pop()
            cards_dealt.append(card)
        return cards_dealt

    shuffle()
    card = deal(1)[0]

    print(card[1]["value"])