#!/usr/bin/env python

from socket import *
from threading import *
import click


def connScan(host, port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        click.secho(f'[+] {port}/tcp Open', fg='green')
    except:
        click.secho(f'[-] {port}/tcp Closed', fg='red')
    finally:
        sock.close()


def portScan(host, ports):
    try:
        tgtIP = gethostbyname(host)
    except:
        print(f'Unknown host {host}')
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan Results For: ' + tgtName[0])
    except:
        print('[+] Scan Results for: ' + str(tgtIP))
    setdefaulttimeout(1)
    for tgtPort in ports:
        t = Thread(target=connScan, args=(host, int(tgtPort)))
        t.start()


@click.command()
@click.option('--host', '-H', type=str, help='specify target host')
@click.option('--port', '-p', type=str, help='specify target port separated by comma')
def main(host, port):
    if (host == None) or (port == None):
        click.secho('erroR: No target or ports specified', fg='red', bold=True)
        exit(0)

    ports = port.split(',')
    if len(ports) <= 1 and ports[0].startswith('+'):
        ports = [*range(1, int(ports[0]) + 1)]
    portScan(host, ports)


if __name__ == '__main__':
    main()
