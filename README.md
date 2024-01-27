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
- 

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
- [Blackjack Live Link](https://p3-blackjack-e37a57443a78.herokuapp.com/)

## Credits

### Content
- Code Institute for the template code
- The geeksforgeeks website for guidance when compiling the steps for the blackjack game (https://www.geeksforgeeks.org/).