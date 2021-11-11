#!/usr/bin/env python

import click

@click.command()
@click.argument('file', type=click.Path(exists=True))
def main(file):
    # cat that file
    with open(file, 'r') as fp:
        click.echo(fp.read())

if __name__ == '__main__':
    main()
