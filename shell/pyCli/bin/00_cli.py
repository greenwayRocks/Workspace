import sys

def main():
    filename = sys.argv[0]
    
    # print it!
    print(f'The arguments are: {sys.argv}')
    print(f'The filename is: {filename}')

    # open this script and read it! @@
    print('\n---')
    with open(filename, 'r') as fp:
        print(fp.read())
    print('---\n')

if __name__ == '__main__':
    main()
