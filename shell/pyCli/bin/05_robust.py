#! /usr/bin/env python3

import sys
import json
import click

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    with open(filename, 'r') as fp:
        click.echo(formatter(fp.read()))

if __name__ == '__main__':
    main()
