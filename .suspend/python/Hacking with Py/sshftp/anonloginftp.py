#!/usr/bin/python

import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print('[+] ' + hostname + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception, e:
        print('[-] ' + hostname + 'FTP Anonymous Logon Failed.')


host = input('Enter the IP Address: ')
anonlogin(host)
