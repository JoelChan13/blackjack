# Blackjack
Blackjack is a python terminal game, which runs in the Code Institute mock terminal on Heroku. The main goal of this game is to reach a total of 21, which is also known as Blackjack, if neither the player nor the computer reach 21, the closest to 21, wins the game. The King, Queen, and Jack cards have a value of 10, while the Ace cards have a value of 11 when drawn and if the dealer goes over 21 through the use of an Ace, the value changes to 1. 

[Blackjack Live Link](https://p3-blackjack-e37a57443a78.herokuapp.com/)

![Responsive Mockup]( https://github.com/JoelChan13/blackjack/blob/main/images/p3-blackjack-mockup.jpg)

## How to Play
- The player chooses how many games s/he wants to play in the input field.
- The player and the dealer are presented with two cards, the player's hand is uncovered whilst the dealer's hand is only partially revealed, as one of the cards is left hidden.
- The player is then prompted to either Hit, by submitting Hit or H in the input field, or Stand, by submitting Stand or S.
- If the user submits a different data type, the same prompt is presented until the correct data is submitted.
- Once the player stands, the dealer's hand is revealed and the dealer will keep on hitting until the total value of the dealer's hand reaches a minimum of 17.
- If both the player and the dealer end up with the same total, a tie is declared.
- Once the winner of the hand is determined, the game moves on to the next game until the number of games selected by the user is completed.
- The total score is presented after all the games have been played.

## Features

### Existing Features
- Ability to play against a computer.
- Select number of games to be played before determining total wins.
- Random card shuffling & dealing.
- Ability to hide one of the dealer's cards.
- Ability for the dealer to automatically keep hitting cards until reaching a minimum of 17 as a total value.
- Accepts user input.
- Maintains a score.
- Ability to change card value based on certain game conditions, such as switching the value of the Ace from 11 to 1 accordingly.
- Input validation & error checking with prompts to enter correct data.

![Games To Play]( https://github.com/JoelChan13/blackjack/blob/main/images/games-to-play.jpg)

![Overall Result]( https://github.com/JoelChan13/blackjack/blob/main/images/overall-result.jpg)

### Future Features
- Add ASCII art to the cards to add immersiveness to the game.
- Add a 5 second timer when it's the player's turn, if no input is provided, player stands automatically.

## Data Model
- 4 classes were created: Card, Deck, Hand, Game
- The Card class contains the suit and the rank of the card represented in the game.
- The Deck class contains all the suits in the game and all the ranks, whereby a for loop append the respective suit to the rank in order to compile a complete deck of cards. in this class one can find the functions shuffle and deal. The The shuffle method shuffles the cards in the deck. It first checks if the number of cards in the deck is greater than 1. If the number of cards is greater than 1, the random.shuffle function is called to shuffle the cards in the deck. The deal method deals a specified number of cards from the deck. It first creates an empty list called cards_dealt. The for loop iterates number times, where number is the number of cards to deal. If the number of cards in the deck is greater than 0, the pop method is called to remove the top card from the deck and assign it to the variable card. The card variable is then appended to the cards_dealt list. After all the cards have been dealt, the cards_dealt list is returned.
- The Hand class has several functions related to how the dealer or player decide to play. The init method is the constructor for the Hand class. It initializes the cards, value, and dealer attributes. The add_card method adds a list of cards to the cards attribute using the extend method. The calculate_value method calculates the value of the hand by iterating over the cards attribute and adding up the values of each card. If an ace is present in the hand and the total value exceeds 21, the value of the ace is reduced by 10. The get_value method calculates the value of the hand using the calculate_value method and returns the value. The is_blackjack method determines whether the hand has a blackjack - a total value of 21. The display method displays information about the hand. If the hand belongs to the dealer and show_all_dealer_cards is False, the second card is hidden. If the hand does not belong to the dealer, the value of the hand is displayed. This class is particularly important as it calculates the value of the hand and displays information about the hand.
- The Game class has functions related to the way the game works. The init method is the constructor for the Game class. It initializes the player_wins, dealer_wins, and ties attributes. The play method starts a new game. It prompts the user to enter the number of games to play and checks if the input is valid. It also creates a new deck of cards, shuffles the deck, and deals two cards to the player and two cards to the dealer. Once the number of games has been decided, the player is prompted to hit or stand until the player's hand value is 21 or greater. In this function the player's hand is displayed whilst only one card from dealer's hand is displayed. Finally this function, checks if the player or the dealer has won the game. This class is particularly important as it perform operations such as dealing cards, calculating the value of a hand, and determining the winner of a game.


## Testing
- The game was tested on multiple browsers, including Firefox, Chrome, Brave, Edge, and Safari.
- Wrong inputs were submitted to check if the game responds correctly.
- Tested in local terminal and Code Institute Heroku terminal

![Wrong Input]( https://github.com/JoelChan13/blackjack/blob/main/images/wrong-input.jpg)

![Overall Result]( https://github.com/JoelChan13/blackjack/blob/main/images/overall-result.jpg)

### Validator Testing
- Testing was done through PEP8 linter and the result was satisfactory

![PEP8 Validation]( https://github.com/JoelChan13/blackjack/blob/main/images/validator-result.jpg)

#### Functional Testing
| Action  | Expected Outcome  | Pass/Fail |
| :------------ |:---------------:| -----:|
| Submit number of games to play| Starts the number of games chosen        |    Pass |
| Submit wrong input when prompted for games to play | Re-ask question        |    Pass |
| Submit hit | Player dealt another card        |    Pass |
| Submit stand | Switches to dealer to finish the game        |    Pass |
| Go bust if the total score is over the value of 21 | Player or dealer lose game if they go over 21 - game ends and winner declared        |    Pass |
| Complete games | Total score presented and winner declared        |    Pass |

## Deployment
- The project was deployed using the Code Institute mock terminal for Heroku, after the Heroku app was linked to the GitHub repository.

## Credits

### Content
- Code Institute for the template code
- The geeksforgeeks website for guidance when compiling the steps for the blackjack game (https://www.geeksforgeeks.org/).