import gspread
from google.oauth2.service_account import Credentials
import random

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
hangman_stage =  ["""
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
                    ----------
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
                    """
    ]

