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

![Wrong Input]( https://github.com/JoelChan13/blackjack/blob/main/images/p3-blackjack-mockup.jpg)

![Wrong Input]( https://github.com/JoelChan13/blackjack/blob/main/images/p3-blackjack-mockup.jpg)

### Future Features
- Add ASCII art to the cards to add immersiveness to the game.
- Add a 5 second timer when it's the player's turn, if no input is provided, player stands automatically.

## Data Model
- 

## Testing
- The game was tested on multiple browsers, including Firefox, Chrome, Brave, Edge, and Safari.
- Wrong inputs were submitted to check if the game responds correctly.
- Tested in local terminal and Code Institute Heroku terminal

![Wrong Input]( https://github.com/JoelChan13/blackjack/blob/main/images/p3-blackjack-mockup.jpg)

### Validator Testing
- Testing was done through PEP8 linter and the result was satisfactory
![PEP8 Validation]()

#### Functional Testing
| Action  | Expected Outcome  | Pass/Fail |
| :------------ |:---------------:| -----:|
| Click on start button| Go to wound-care-trivia.html/start quiz & shuffles questions and answers        |    Pass |
| Click on high scores button | Go to highscores.html        |    Pass |
| Input Username | Stores username in local storage        |    Pass |
| Click on correct answer | Highlights answer button in green and displays rationale and next button        |    Pass |
| Click on incorrect answer | Highlights answer button in red and displays rationale and next button        |    Pass |
| Click on next button | Displays following question, and once all questions have been answered displays result page        |    Pass |
| Click on retry button | Restarts quiz        |    Pass |
| Click on return to home button | Redirects user to home page/index.html        |    Pass |
| Hover over answer buttons | highlights buttons in different colour and changes the cursor to a pointer        |    Pass |
| Hover over Recipes answer button once answer is submitted | Changes cursor to a no symbol         |    Pass |

## Deployment
- The site was deployed to GitHub pages. From the GitHub repository, access wound-care-trivia. Click on the deployments section. Click on the active deployment link provided.
- [Blackjack Live Link](https://p3-blackjack-e37a57443a78.herokuapp.com/)

## Credits

### Content
- Boilerplate HTML Structure Code was taken from the ci-full-template found in CI GitHub repo by lechien73
- The information related to wound care, found in the rationale of every answer was obtained from The British Journal of Nursing.