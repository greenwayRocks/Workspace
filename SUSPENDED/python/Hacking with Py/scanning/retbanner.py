#!/usr/bin/env python3

import socket
import click


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode('utf-8').strip('\n')
        return banner
    except:
        return
    finally:
        sock.close()


@click.command()
@click.option('--host', '-H', type=str, help='specify target host')
@click.option('--port', '-p', type=str, default='22', help='specify target ports sep by commas')
def main(host, port):
    if (host == None) or (port == None):
        click.secho('erroR: No target or ports specified', fg='red', bold=True)
        exit(0)

    ports = port.split(',')
    if len(ports) <= 1 and ports[0].startswith('+'):
        ports = [*range(1, int(ports[0]) + 1)]
    for port in ports:
        banner = retBanner(host, port)
        if banner:
            click.secho(f'[+] {host}:  {str(port)} {banner}', fg='green')
        else:
            click.secho(f'[+] {host}:  {(port)} {banner}', fg='red')


if __name__ == '__main__':
    main()
