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
PLAY_AGAIN_MSG = f"""{Fore.RED}
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


def game(word):
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
    while not guessed and lives > 0:
        print(f"\n\tWRONG LETTERS GUESSED:\n\t{guessed_wrong}\n")
        display_score(score)
        print("\n")
        if lives > 1:
            print(f"\n\tYOU HAVE {lives} LIVES")
        else:
            print(f"\n\tYOU HAVE {lives} LIVES LEFT\n")
        guess = input(f"""\t\t
        GUESS A LETTER OR A WORD PLEASE:\n\t>>> """).upper()
        print("\n")
        #Check if the player has already guess the letter
        # Or if the letter guessed in not in the word
        # And if the letter guessed is in the word
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"""\n\t
                YOU HAVE ALREADY GUESSED THIS LETTER {guess}\n""")
            elif guess not in word:
                print(f"""\n\t
                {guess} IS NOT IN THE WORD. TRY ANOTHER ONE!\n""")
                lives -= 1
                guessed_letters.append(guess)
                guessed_wrong.append(guess)
            else:
                print(f"""\n\t
                GREAT, {guess} IS IN THE WORD! KEEP GOING!\n""")
                guessed_letters.append(guess)
                guessed_right += 1
                score += CORRECT_ANSWER
                word_as_list = list(full_word)
                indices = [i for i, letter in enumerate(
                          word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                full_word = "".join(word_as_list)
                if "_" not in full_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"""\n\t
                YOU HAVE GUESSED THE WORD {guess} ALREADY.""")
            elif guess != word:
                print(f"\n\t{guess}, IS NOT THE WORD. TRY AGAIN!")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                full_word = word
        else:
            print(f"\n\tIS NOT VALID GUESS.\n")
        print(display_hangman(lives))
        word_space(f"\t{full_word}")
        print("\n")
    result(guessed, word, guessed_right, score)


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


def update_scoreboard(data, score):
    """
    This updates a new row with the name, score and difficulty in worksheet.
    """
    print(f"\t{Fore.GREEN}Updating Leaderboard...\n")
    worksheet_to_update = SHEET.worksheet("scoreboard")
    worksheet_to_update.append_row([
      str(player_name[0:7]), score, difficulty])
    print(f"\t{Fore.GREEN}Leaderboard Update successful.\n")


def display_scoreboard():
    """
    Displays to the players the 10 best scores
    """
    score_sheet = SHEET.worksheet("scoreboard").get_all_values()[1:]
    for data in score_sheet:
        data[1] = (data[1])

    update_data = sorted(score_sheet, key=lambda x: int(x[1]), reverse=True)

    print(f"{rules()}")
    if (len(update_data) < 10):
        count = len(update_data)
    else:
        count = 10

    for i in range(0, count):
        print(f"""
        {Fore.GREEN}{i+1}\t{update_data[i][0]}\t  {update_data[i][1]}\t{
        update_data[i][2]}\t{update_data[i][3]}""")


def result(guessed, word, guessed_right, score):
    """
    Display win or lose message
    """
    if guessed and len(word) >= 6 and guessed_right <= 3:
        print(f"""{Fore.GREEN}
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
        \n""")
        print(f"""{Fore.GREEN}
        YOU WIN {player_name}, YOU HAVE GUESSED THE WORD COMPLETELY AT ONCE!\n
        """)
        score = score + CORRECT_ANSWER + CORRECT_FULLWORD
    elif guessed:
        print(f"""{Fore.RED}
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝       
        \n""")
        print(f"""{Fore.RED}
        YOU WIN {player_name}, YOU HAVE GUESSED THE RIGHT WORD!\n""")
        score = score + CORRECT_ANSWER
    else:
        print(f"""{Fore.RED}
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝       
        """)
        print(F"""{Fore.RED}
        YOU LOSE {player_name}, THE RIGHT WORD WAS {word}!
        """)
    update_scoreboard(data, score)
    display_score(score)


def main():
    """
    Starts the game with a random word.
    Once a game run is complete, give to the player 3 choices at the end:
        * Play again
        * Leaderboard
        * Exit the game
    """

    play_game = True
    while True:
        if play_game:
            word = get_word()
            game(word)

        user_input = input(f"{PLAY_AGAIN_MSG}>>> ").lower()
        if user_input == "a":
            print(f"\n\tYou have decided to continue playing the game.\n")
            play_game = True
        elif user_input == "b":
            display_scoreboard()
            play_game = False
        elif user_input == "c":
            print(f"{Fore.RED}\n\tNow closing the game...")
            print(f"""{Fore.CYAN}
            \n\tThanks for playing, {player_name.capitalize()}.
            \n\tHope to see you again soon!\n""")
            #sys.exit()
        else:
            print(f"""{Fore.YELLOW}\n\t
            That is not a valid option. Please try again.\n""")
            play_game = False


if __name__ == '__main__':

    # Allows the user to input their own name and city to play the game
    while True:
        player_name = input(f"\n{Fore.CYAN}NAME:\n>>> ").strip().upper()
        if len(player_name) == 0:
            print(f"{Fore.RED}This is not a valid name!")
            continue
        else:
            break
    while True:
        player_city = input(f"{Fore.CYAN}YOUR CITY:\n>>> ").strip().upper()
        if len(player_city) == 0:
            print(f"{Fore.RED}This is not a valid city!")
            continue
        else:
            break
    print(f"""{Fore.YELLOW}\n\t
    HELLO {player_name}, WELCOME TO THE HANGMAN GAME!\n""")
    print(f"{Fore.BLUE}{rules()}")
    input(f"""\n{Fore.CYAN}
    {player_name}, PRESS ANY KEY TO START THE GAME.\n    >>> """)

    main()