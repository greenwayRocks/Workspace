#! /usr/bin/env python3

import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)

    # dump as string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main():
    parser = argparse.ArgumentParser(prog="jformat", description="Json file formatter on the fly!")
    parser.add_argument('--file', '-f', help='path to a JSON file')

    args = parser.parse_args()

    if args.file:
        ## open json file
        with open(args.file, 'r') as fp:
            print(formatter(fp.read()))
    else:
        print('Boo! No file passed in; can\'t format anything!')

if __name__ == '__main__':
    main()
