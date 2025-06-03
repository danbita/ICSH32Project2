#connectfour_common_functions

'''
This module contains shared methods from connectfour_shell.py
and connectfour_server.py
'''

from connectfour import *

def start_game() -> GameState:
    '''
    Starts the game by having the user choose the number of rows and columns
    Checks that the columns and rows chosen are valid
    '''
    board_size = input('How many columns and rows would you like? (format: "c r") ')
    board_size = board_size.split()
    while len(board_size) < 2:
        print('That was an invalid input')
        board_size = input('How many columns and rows would you like? (format: "c r") ')
        board_size = board_size.split()
    try:
        return new_game(int(board_size[0]), int(board_size[1]))
    except ValueError:
        print('Either your row or column value is invalid. Try again.')
        return start_game()

def board_full(game: GameState) -> bool:
    '''
    determines whether the board is full or not
    if false, player move is drop
    if true, player move is pop
    '''
    total = 0
    for col in game.board:
        for row in col:
            if row != EMPTY:
                total += 1
    if total == rows(game) * columns(game):
        return True
    else:
        return False

def print_board(board: GameState) -> None:
    '''
    prints out the board
    '''
    labels = ''
    for col in range(1, columns(board) + 1):
        if columns(board) < 10:
            labels += (str(col) + ' ')
        else:
            if col < 10:
                labels += (str(col) + '  ')
            else:
                labels += (str(col) + ' ')
    print(labels)
    spacing = ' '
    if columns(board) >= 10:
        spacing = '  '
    for row in range(0, rows(board)):
        line = ''
        for col in board.board:
            if col[row] == EMPTY:
                line += (('.') + spacing)
            elif col[row] == RED:
                line += ('R' + spacing)
            else:
                line += ('Y' + spacing)
            
        print(line)

def move_choice(game: GameState) -> str:
    '''
    User chooses whether to DROP or POP
    '''
    choice = input('Choose "DROP" or "POP": ')
    if not choice == 'DROP' and not choice == 'POP':
        print('Not a valid response. Try again.')
        return move_choice(game)
    elif choice == 'DROP' and board_full(game):
        print('Board is full so drop is not a valid move')
        return move_choice(game)
    return choice

