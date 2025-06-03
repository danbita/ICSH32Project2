#connectfour_server.py


'''
This module runs the connect 4 game with the user playing against a server
'''


from connectfour import *
from connectfour_socket_handling import *
from connectfour_common_functions import *

def make_move(game: GameState, choice: str, move: int) -> GameState:
    '''
    Drops or pops a piece in a column, depending on the user choice
    Ensures the column is a valid one
    '''
    if choice == 'POP':
        return pop(game, move - 1)
    else:
        return drop(game, move - 1)

def try_move(connection: 'connection', game: GameState, choice: str) -> str:
    '''
    Tries placing a move to see if it is valid
    If it is it sends the move to the server
    '''
    move = input('Choose a col to place a piece: ')
    try:
        test = int(move)
    except:
        print('Invalid input')
        return try_move(connection, game)
    if choice == 'POP':
        write_out(connection, ('POP ' + move))
        return int(move)
    elif choice == 'DROP':
        write_out(connection, ('DROP ' + move))
        return int(move)

def run():
    '''
    runs the game
    '''
    connection = connect('circinus-32.ics.uci.edu', 4444)
    username = input('Choose a username: ')
    write_out(connection, 'I32CFSP_HELLO ' + username)
    response = read_response(connection)
    print(response)
    c4game = start_game()
    write_out(connection, 'AI_GAME ' + str(columns(c4game)) + ' ' + str(rows(c4game)))
    response = read_response(connection)
    print(response)
    game_alr_over = 0
    while winner(c4game) == EMPTY:
        if c4game.turn == RED:
            choice = move_choice(c4game)
            move = try_move(connection, c4game, choice)
            response = read_response(connection)
            while(response == 'INVALID'):
                print(response)
                response = read_response(connection)
                print(response)
                choice = move_choice(c4game)
                move = try_move(connection, c4game, choice)
            c4game = make_move(c4game, choice, move)
        else:
            if response == 'OKAY':
                print(response)
            response = read_response(connection)
            if response == 'OKAY':
                print(response)
                response = read_response(connection)
            print(response)
            response = response.split()
            try:
                c4game = make_move(c4game, response[0], int(response[1]))
            except:
                print('Socket had an invalid input. Game over')
                game_alr_over = 1
                close(connection)
                break
            response = read_response(connection)
            print(response)
        print_board(c4game)
    if game_alr_over == 0:
        close(connection)
                                
if __name__ == '__main__':
    run()

