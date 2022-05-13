import os

from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import users_inputs

from applications_tools.games.Coin_flipping.Main_Coin_flipping import coin_flip
from applications_tools.games.Hangman.Main_Hangman import Hangman_game

def games():
    print("""So you want to play some games huh??
Here is what i got for you:
    1- 2048
    2- Coin flip
    3- Hangman
    4- Pong""")
    users_input = users_inputs(0,4)
    if users_input == 1:
        os.system("python3 puzzle.py")
    elif users_input == 2:
        coin_flip()
    elif users_input == 3:
        Hangman_game()
    elif users_input == 4:
        os.system("python3 $(pwd)/applications_tools/games/Pong/Main_pong.py")