#connectfour_shell.py

'''
This module runs the connect 4 game using only python shell interaction
'''

from connectfour import *
from connectfour_common_functions import *

def make_move(game: GameState) -> GameState:
    '''
    Drops or pops a piece in a column, depending on if the board is full
    Ensures the column is a valid one
    '''
    choice = move_choice(game)
    move = input('What column would you like to play a piece in? ')
    try:
        if choice == 'POP':
            return pop(game, int(move) - 1)
        elif choice == 'DROP':
            return drop(game, int(move) - 1)
    except ValueError:
        print("That's not a valid column. Try again.")
        return make_move(game)
    except InvalidMoveError:
        print('That move is invalid. Choose another.')
        return make_move(game)

def run() -> None:
    '''
    runs the game
    '''
    c4game = start_game()
    while winner(c4game) == EMPTY:
        print_board(c4game)
        c4game = make_move(c4game)
    print_board(c4game)
    if winner(c4game) == RED:
        print('Red wins')
    else:
        print('Yellow wins')

if __name__ == '__main__':
    run()
