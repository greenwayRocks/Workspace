#!/usr/bin/python
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# My Scanner function


def scanner(host, port):
    if sock.connect_ex((host, port)):
        print(f'Port {port} is closed!')
    else:
        print(f'Port {port} is open!')


# Defining values
host = '192.168.1.103'
port = 22

# Parsing command-line values
if len(sys.argv) > 1:
    host = sys.argv[1]
    port = int(sys.argv[2])

if __name__ == '__main__':
    scanner(host, port)
