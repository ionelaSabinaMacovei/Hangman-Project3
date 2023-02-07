import gspread
from google.oauth2.service_account import Credentials
from words import words
import random

import colorama
from colorama import Fore
colorama.init(autoreset=True)

SCOPE = [  
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scoreboard')

scoreboard = SHEET.worksheet("scoreboard")

data = scoreboard.get_all_values()

#consts
CORRECT_ANSWER = 25
CORRECT_FULLWORD = 200
PLAY_AGAIN_MSG = f"""{Fore.CYAN}
A - PLAY AGAIN
B - LEADERBOARD
C - EXIT THE GAME
"""


def display_hangman(lives):
    """
    This is an image of how many lives the user has left
    before the game is over."""
    hangman_stage = ["""
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |     / \\
                        -
                        """,
                        
                        """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |     /
                        -
                        """,
                    
                        """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |
                        -
                        """,
                        
                        """
                        --------
                        |      |
                        |      O
                        |     \\|
                        |      |
                        |
                        -
                        """,
                        
                        """
                        --------
                        |      |
                        |      O
                        |      |
                        |      |
                        |
                        -
                        """,
                        
                        """
                        --------
                        |      |
                        |      O
                        |
                        |
                        |
                        -
                        """,
                        
                        """
                        --------
                        |      |
                        |
                        |
                        |
                        |
                        -
                        """,
                        """
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            ----------
                        """,
                        """




                            |
                            |
                            ----------
                        """]
    return hangman_stage[lives]


def rules():
    """
    Rules of the game
    """
    print(f"""\n   {Fore.RED}RULES
    1. Choose the difficulty of the game:
         - Easy = 8 lives
         - Medium = 6 lives
         - Hard = 4 lives
    
    2. Try to guess the one of the letters in the word!
        - If the letter is in the word, it will show up in the word.
        - If the letter is not in the word, you will be notify that is not the correct letter and you will lose a life.
    
    3. You WIN by guessing the full word and saving HangMan.

    4. You LOSE if you run out of lives and HangMan is hung

    """)


def intro_game():
    """
    Logo of the game and rules
    """

    print(f"""{Fore.RED}

 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░

\n""")

    print(f"Welcome to the Hangman Game!\n")


def get_word():
    """
    Get a random word from the words list
    """
    nm = random.randint(0, len(words)-1)
    word = words[nm]
    return word


def play_game(word):
    """
    Game main function
    """
    full_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    guessed_wrong = []
    guessed_right = 0
    lives = 7
    score = 0
    print(f"\n\tLET'S PLAY THE HANGMAN GAME!\n")
    print(f"""\tYOU WORD CONTAINS {len(word)} LETTERS""")
    print(display_hangman(lives))
    word_space(f"\t{full_word}")
    print("\n")


def word_space(full_word):
    """
    Add space in between letters in the random word
    """
    for i in full_word:
        print(i, end=" ")


def display_score(score):
    """
    Display player score during the game
    """
    print(f"\tSCORE: {score}")


