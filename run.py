
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
