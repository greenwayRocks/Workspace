#!/usr/bin/env python3
import os


def main():
    for root, dirs, files in os.walK('.'):
        full_root = os.path.abspath(root)
        print(f'Checking dir {full_root}')
        print('\tSubfolders: ' + str(dirs))
        print(f'\tFiles: ' + str(files))
        print()


if __name__ == '__main__':
    main()
