import gspread
from google.oauth2.service_account import Credentials
import os 
from words import words

SCOPE = [  
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Scoreboard')

global guesses
global invalid_option
guesses = []  # previously guessed letters
invalid_option = """WHOOPS! That is not a valid option!\n
Please enter a valid option, using the number
which corresponds to your selection\n"""

class colors:  
    # print to terminal in different colors
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    GREEN = "\033[0;32m"


def clear_console():
    """
    Function for clearing the terminal screen
    """
    os.system('clear')



"""
Array of hangman visuals to print
"""
hangman_stage =  ("""
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
                    """ )

def rules():
    """
    Rules of the game
    """
    print(f"""\n   {colors.RED}RULES
    1. Choose the difficulty of the game:
         - Easy = 8 lives
         - Medium = 6 lives
         - Hard = 4 lives
    
    2. Try to guess the one of the letters in the word!
        - If the letter is in the word, it will show up in the word.
        - If the letter is not in the word, you will be notify that is not the correct letter and you will lose a life.
    
    3. You WIN by guessing the full word and saving HangMan.

    4. You LOSE if you run out of lives and HangMan is hung

    Choose one of the option: 
    
    {colors.GREEN}1. Play Game
    {colors.BLUE} 2. Scoreboard
    """)
