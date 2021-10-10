import socket
import requests

def check_localhost():
    '''Checks localhost connectivity'''
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    '''Checks internet connectivity'''
    res = requests.get('https://www.google.com')
    return res.status_code == 200
