#!/usr/bin/env python3

from socket import *
from threading import *
import click


def connScan(host, port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        banner = sock.recv(1024).decode('utf-8').strip('\n')
        click.secho(f'[+] {port:>5}/tcp   Open - {banner}', fg='green')
    except:
        click.secho(f'[-] {port:>5}/tcp Closed', fg='red')
    finally:
        sock.close()


def portScan(host, ports):
    # Socket connection getHost IP and Name
    try:
        tgtIP = gethostbyname(host)
    except:
        click.secho(f'Unknown Host: {host}', fg='red', bold=True)
    try:
        tgtName = gethostbyaddr(tgtIP)
        click.secho(
            f'[*] Scan Results for: {tgtName[0]}', bg='blue', fg='white')
        print()
    except:
        click.secho(
            f'[*] Scan Results for: {tgtIP}', bg='blue', fg='white')
        print()
    # Threading for port scans
    for port in ports:
        t = Thread(target=connScan, args=(host, int(port)))
        t.start()


@click.command()
@click.option('--host', '-H', type=str, help='specify a target host')
@click.option('--port', '-p', type=str, help='target ports separated by commas')
def main(host, port):
    click.secho('Port Scanner v1.0', bold=True, fg='green')

    # Check if supplied with target IP and Port
    if (host == None) or (port == None):
        click.secho('erroR: No target or ports specified', fg='red', bold=True)
        exit(0)

    # Parse ports
    ports = port.split(',')
    if len(ports) <= 1 and ports[0].startswith('+'):
        ports = [*range(1, int(ports[0]) + 1)]

    portScan(host, ports)


if __name__ == '__main__':
    main()
