#! /usr/bin/env python3

import sys
import json

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)

    # dump as string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main():
    filename = sys.argv[-1]

    ## printing info
    print(f'Arguments to this file are: {sys.argv}')
    print(f'The filename would be: {filename}')
    print()

    ## open json file

    with open(filename, 'r') as fp:
        print(formatter(fp.read()))

if __name__ == '__main__':
    main()
