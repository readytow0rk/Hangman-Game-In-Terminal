"""
Project 3 for Code Istitute
"""
import random
import os
from colorama import Fore
import words
from hangman import hangman_lives


MOVIES_THEME = words.movies_words
CARS_THEME = words.cars_words
ANIMALS_THEME = words.animals_words


def clear_terminal():
    """
    function to clean terminal
    """
    os.system(('cls' if os.name == 'nt' else 'clear'))
    title()


def title():
    """
    function to display the title
    """
    print(Fore.RED + """
       ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
       ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
       ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
       ██╔══██║██╔══██║██║╚██╗██║██║   ██║██  ██╔╝██║██╔══██║██║╚██╗██║
       ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """)


def welcome():
    """
    function to display title with navigation to start the game or read rules
    """
    clear_terminal()
    print('\n')
    print(Fore.WHITE + ' 1 PLAY GAME '.center(80))
    print(Fore.WHITE + ' 2 HOW TO PLAY '.center(80))
    print('\n' * 4)
    while True:
        user_choice = input(' ' * 28 + 'Select 1 or 2: ')
        if user_choice == '1':
            start()
        elif user_choice == '2':
            rules()
        else:
            print('Please select 1 or 2'.center(77))
            print('\n')


def rules():
    """
    function to display rules for users
    """
    clear_terminal()
    print(Fore.WHITE + """
       Hangman is a word guessing game.\n
       If the letter is in the unknown word it will display.\n
       If the guessed letter is not in the unknown word you will lose a life.\n
       You can choose the different theme of words, M for movies theme,
       C for cars theme, A for animals theme.\n
       Good luck!
        """)
    input(Fore.GREEN + ' ' * 12 + 'Press enter to return to the main menu\n')
    welcome()


def set_theme():
    """
    function to set the theme of the word
    """
    print('\n')
    print(Fore.WHITE + 'Please select M for movies theme (7 lives)'.center(80))
    print(Fore.WHITE + 'C for cars theme (6 lives), '.center(80))
    print(Fore.WHITE + 'A for animals theme (5 lives)'.center(80))
    theme = False
    lives = ""
    while not theme:
        theme_level = input(' '.center(40)).upper()
        if theme_level == 'M':
            theme = True
            lives = 7
        elif theme_level == 'C':
            theme = True
            lives = 6
        elif theme_level == 'A':
            theme = True
            lives = 5
        else:
            print(Fore.GREEN + 'Please select M, C or A'.center(80))
    return lives


def random_word(lives):
    """
    function to set the random word depending on user theme
    """
    get_words = ""
    if lives == 7:
        get_words = random.choice(MOVIES_THEME).upper()
    elif lives == 6:
        get_words = random.choice(CARS_THEME).upper()
    elif lives == 5:
        get_words = random.choice(ANIMALS_THEME).upper()
    return get_words


def game(word, lives_qv):
    """
    function to set the theme of the game and start
    """
    clear_terminal()
    blanks = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    print(Fore.WHITE + hangman_lives(lives_qv))
    print(Fore.GREEN + " ".join(blanks).center(76))
    print('\n')
    while not guessed and lives_qv > 0:
        print(Fore.WHITE + f"Lives: {lives_qv}".center(76))
        user_guess = input(' ' * 25 + 'Please guess a letter: ').upper()
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                clear_terminal()
                print(' ' * 25 + 'You already guessed ' + user_guess)
            elif user_guess not in word:
                clear_terminal()
                print(' ' * 25 + user_guess + ' is not in the word')
                lives_qv -= 1
                guessed_letters.append(user_guess)
            else:
                clear_terminal()
                print(' ' * 30 + user_guess + ' is in the word')
                guessed_letters.append(user_guess)
                word_li = list(blanks)
                indices = [i for (i, letter) in enumerate(word)
                           if letter == user_guess]
                for index in indices:
                    word_li[index] = user_guess
                blanks = ''.join(word_li)
                if '_' not in blanks:
                    guessed = True
        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess in guessed_word:
                clear_terminal()
                print(' ' * 30 + 'You guessed the word ' + user_guess)
            elif user_guess != word:
                clear_terminal()
                print(' ' * 30 + user_guess + 'is not in the word')
                lives_qv -= 1
                guessed_word.append(user_guess)
            else:
                guessed = True
                blanks = word
        else:
            clear_terminal()
            print(Fore.RED + 'Not valid'.center(80))
        print(Fore.WHITE + hangman_lives(lives_qv))
        print(Fore.GREEN + " ".join(blanks).center(76))
        print('\n')
    restart(guessed, word)


def restart(guessed, word):
    """
    function display results when user guessed the word or lost his lives
    """
    if guessed:
        clear_terminal()
        print()
        print(Fore.GREEN + 'You guessed the word'.center(80))
        print('\n')
        again()
    else:
        clear_terminal()
        print(Fore.WHITE + """
         ██████╗  █████╗ ███╗   ███╗███████╗  ██████╗ ██╗   ██╗███████╗██████╗
         ██╔════╝ ██╔══██╗████╗ ████║██╔════╝ ██╔═══██╗██║  ██║██╔════╝██╔══██╗
         ██║  ███╗███████║██╔████╔██║█████╗   ██║   ██║██║  ██║█████╗  ██████╔╝
         ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝   ██║   ██║╚██╗ ██╔╝██╔══╝ ██╔══██╗
         ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗ ╚██████╔╝ ╚████╔╝ ██████╗██║  ██║
         ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═════╝   ╚═══╝  ╚═════╝╚═╝  ╚═╝
        """)
        print(' ' * 20 + 'You run out of lives. The word was: ' + word)
        print('\n')
        again()


def again():
    """
    function to start the game again or back to the main menu
    """
    while True:
        user_input = input(Fore.WHITE + ' ' * 30 + 'Play again? Y/N').upper()
        print('\n')
        if user_input == 'Y':
            start()
        elif user_input == 'N':
            welcome()
        else:
            print('Please select Y or N'.center(80))


def start():
    """
    function to start the game
    """
    clear_terminal()
    lives_qv = set_theme()
    get_random = random_word(lives_qv)
    game(get_random, lives_qv)


def main_menu():
    """
    function to display main menu
    """
    welcome()


main_menu()
