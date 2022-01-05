#!/usr/bin/env python
import os
import socket
import sys


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8').strip('\n')
        return banner
    except:
        return
    finally:
        s.close()


def checkVulns(banner, filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.strip('\n') in banner:
                print('[+] Server is vulnerable: ' + banner)


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] File does not exist!')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('Access Denied!')
            exit(0)
    else:
        print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
        exit(0)

    portlist = [21, 22, 25, 80, 110, 443, 445]
    for x in range(101, 150):
        ip = '192.168.1.' + str(x)
        for port in portlist:
            banner = retBanner(ip, int(port))
            if banner:
                print('[-] ' + ip + '/' + str(port) + ' : ' + banner)
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()
