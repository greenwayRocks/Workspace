#!/usr/bin/env python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input('[*] Enter The Host To Scan: ')
#port = int(input('[*] Enter The Port To Scan: '))


def scanner(host, port):
    if sock.connect_ex((host, port)):
        print(colored(f'[!!] Port {port} is closed!', 'red'))
    else:
        print(colored(f'[+] Port {port} is open!', 'green'))


if __name__ == '__main__':
    for port in range(1, 1000):
        scanner(host, port)
