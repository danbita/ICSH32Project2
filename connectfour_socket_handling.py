#connectfour_socket_handling.py

'''
This module handles all of the socket related functions for connectfour_server.py
'''

import socket

def connect(host: str, port: int) -> 'connection':
    '''
    Connects to the Connect 4 server
    '''
    my_socket = socket.socket()
    my_socket.connect(('circinus-32.ics.uci.edu', port))
    my_socket_input = my_socket.makefile('r')
    my_socket_output = my_socket.makefile('w')
    return my_socket, my_socket_input, my_socket_output

def write_out(connection: 'connection', message: str):
    '''
    Writes out a message to the Connect 4 server from a connection that is
    assumed to be open and not closed yet
    '''
    my_socket, my_socket_input, my_socket_output = connection
    my_socket_output.write(message + '\r\n')
    my_socket_output.flush()

def read_response(connection: 'connection'):
    '''
    Reads the response from the Connect 4 server from a connection that is assumed
    to be open and not closed yet.   
    '''
    my_socket, my_socket_input, my_socket_output = connection
    return my_socket_input.readline()[:-1]

def close(connection: 'connection'):
    'Closes the connection'
    my_socket, my_socket_input, my_socket_output = connection
    my_socket_input.close()
    my_socket_output.close()
    my_socket.close()
