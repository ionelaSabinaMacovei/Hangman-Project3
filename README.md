# Hangman, Capitals of Europe - Game

# Introduction
This project is based on the game HangMan, this game has been around since 1894 under the name "Birds, Beasts and Fishes".

 The main goal of the game is to guess the full word before hangman is hung. This is done by guessing a letter in the word.

If the guess is right, it is placed in the blank spaces that make up the word. If it is not, the user loses a life. The word must be guessed before the user runs out of lives.

[Live Project Here](https://hangman-project3.herokuapp.com/)

![HangMan Hero Image](images/hangman-logo.jpg)

## Goal

My goal is to utilise my knowledge of python to create a game which gathers user inputs and provides responses based on the input given.

## Table Content


## User Experience - UX

* As a user, I want to:

1. Be able to understand the purpose of the App and start a new game.
2. Be able to follow the score, see the wrong and right letters appear once I take a turn, and see how many tries remain before the game is over.
3. Be able to watch my results and other players' results on the Scoreboard.
4. Be able to play the game again with a different word as chosen by the computer.
5. Be challenged and try to improve on my previous scores. 
6. Compare my scores with other users on the Scoreboard.

## Design

#### Colours
* The colours in the game are supplied by the Python Colorama Model

### Flowcharts
I designed this project on the basis of the below flowchart.I created flowcharts to assist me with the logical flow throughout the application. The charts were generated using [Lucidchart](https://lucid.app/) 

![Flowcharts](images/flowchart-hangman.png)


## Features

### Logo and Intro Message

![Logo and Intro Message](images/logo-intro-message.png)

* When the users reach the website, they will see this feature. The game logo and the intro message are displayed here.<br>

### Game Rules
![Game Rules](images/rules.png)
* After the user inputs their name, the program will display the game rules. The player then presses any key to start the game.<br>

## Game Features

### Hangman Stage 1
![Game Feature](images/stage1-hangman.png)<br><br>

This feature displays where the main scene happens. Here the user can play and see the following information about the game:
* Numbers of letters chosen by the computer 
* Hangman stages
* Letters guessed right
* Letters guessed wrong
* Current score
* Current number of lives
* Input to guess a letter or a full word

![Hangman Stage](images/stage2-hangman.png)<br><br>
![Hangman Stage](images/stage3-hangman.png)<br><br>
Any time the player guesses a wrong letter, a part of the hangman appears

### Hangman Lose

![Hangman Lose](images/lose-hangman.png)
* 7 letters guessed wrong the player will see the full hangman and the game is over.

### Hangman Win

![Hangman Win](images/win-hangman.png)
* If the player guessed the full word letter by letter, they will see this feature and will win the game.

### Hangman Win Full Word

![Hangman Win Full Word](images/win-fullword-hangman.png)
* If the player guessed all the letters that appear in the word thereby completing the word or at least guessing no more than 3 correct letters before completing the full word, this feature will appear.

### Menu Options

![Menu Options](images/menu-hangman.png)
* In the end of the game users will have access to the menu where they can choose from these options: <br>
[A] - Play Again <br>
[B] - Leaderboard <br>
[C] - Exit Game

### Scoreboard
![Scoreboard](images/scoreboard-hangman.png)
* The Scoreboard shows the 10 players with the best scores.

### Exit Game
![Exit Game](images/close-hangman.png)
* The players will see this message if they will chose to exit the game by typing [C].

## Storage Data

I have used a Google sheet to save the player name and score.  This sheet is connected to the code through the Google Drive and Google Sheet API by the Google Cloud Platform. This method allows me to send and receive data as I had access to the Google Sheet API credentials. I also added in the Config Vars to these credentials when I was deploying the project in Heroku. As this is sensitive data, I had to add the creds.json in the Git ignore file. This would ensure that these credentials are not pushed to the repository.

### Code to Connect to Google Sheet

![Code to Connect to Google Sheet](images/connect-google-sheets.png)

### Google Sheet Hangman Scoreboard

![Google Sheet Hangman Scoreboard](images/google-sheets.png)

## Testing

### PEP 8 Online

The [PEP8](https://pep8ci.herokuapp.com/) Validator Service was used to validate every Python file in the project to ensure there were no syntax errors in the project.

![PEP8](images/pep8-validator.png).
* No errors or warnings were found during the testing of the code in PEP8

### Lighthouse 

 Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on the Desktop.

* Desktop Results:

  ![Lighthouse Result](images/light-house-result.png)

    ## Functionality 
* The terminal has no issues and is working properly. 
* The input for name work properly and shows the user an alert if the input is empty.
* The game rules appear without any issues after the player submits their name.
* The option to press any key to start a game is running well. 
* At the end of the game, the Leaderboard is updating correctly.
* All the menu options are working without any fails.

## Bugs
