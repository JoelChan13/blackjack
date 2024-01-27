# Blackjack
Blackjack is a python terminal game, which runs in the Code Institute mock terminal on Heroku. The main goal of this game is to reach a total of 21, which is also known as Blackjack

[Blackjack Live Link](https://p3-blackjack-e37a57443a78.herokuapp.com/)

![Responsive Mockup]( https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/wound-care-trivia-index-mockup.jpg)

## Features

### Start
- The start button is featured at the center of the home page and prompts the commencement of the quiz.
- Upon commencing the quiz, the user is prompted to submit a username, which is stored in the local storage.

### High Scores
- The high scores button is featured at the center of the home page, below the Start button and directs the user to the high scores page.
- On pressing the high scores button, the user is taken to the high scores page, which retrieves the top 5 results, together with their respective username, from the local storage.

![Start & High Score Buttons](https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/wound-care-trivia-index-mockup.jpg)

![High Scores Page]( https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/wound-care-trivia-highscores-mockup.png)

### Answer Selection & Next Buttons
- The answers are shuffled and can be selected by clicking on them.
- Upon clicking the selected answer, the answer will turn green, if correct, or red, if incorrect, whilst also presenting the next button.
- The user is not allowed to press any other answer once the selection has been made.
- A rationale, highlighted in green, is provided after every answer is submitted to provide further information to the user.
- The font colour and background have been chosen accordingly to ensure better readability.
- A rationale, highlighted in green, is provided after every answer is submitted to provide further information to the user.

![Answer Selection & Rationale]( https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/wound-care-trivia-answer-mockup.png)

### Result & Return to Home Page
- The user is presented with the result once all questions have been answered and a prompt to retry the quiz or return to home is presented.
- By clicking the retry button, the user restarts the quiz and is prompted to provide a username.
- By clicking the return to home button, the user is taken to the home page.

![Result]( https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/wound-care-trivia-result-mockup.jpg)

## Testing
- The page was tested on multiple browsers, including Firefox, Chrome, Brave, Edge, and Safari.
- The project is responsive and fully functional in all standard screen sizes.
- Testing was conducted to ensure ease of readability on different devices.

### Validator Testing
#### HTML
- No errors were returned when testing all sections of the project through the W3C validation.
#### CSS  
- No errors were returned when testing styling section of the project through the W3C validation.
#### Accessibility
- Testing was done through Lighthouse DevTool and the result was satisfactory
![Lighthouse Validation](https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/lighthouse-result-1.jpg)

![Lighthouse Validation](https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/lighthouse-result-2.jpg)

![Lighthouse Validation](https://github.com/JoelChan13/wound-care-trivia/blob/main/assets/images/lighthouse-result-3.jpg)

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
- [Wound Care Trivia Link](https://joelchan13.github.io/wound-care-trivia/)

### Local Deployment
- The repository was cloned to local machine using the following command in the terminal: git clone <https://github.com/JoelChan13/wound-care-trivia.git>
- The following command was submitted in the terminal: cd wound-care-trivia.
- index.html was opened in the browser to start website.


## Credits

### Content
- Boilerplate HTML Structure Code was taken from the ci-full-template found in CI GitHub repo by lechien73
- The information related to wound care, found in the rationale of every answer was obtained from The British Journal of Nursing.