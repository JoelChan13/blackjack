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

cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
random.shuffle(cards)

"""
Removes a single element from the cards list to emulate the dealer 
dealing a card from the deck
"""
card = cards.pop
print(cards)
