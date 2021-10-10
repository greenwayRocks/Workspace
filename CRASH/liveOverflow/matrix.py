# Python command-line args
import sys

if len(sys.argv) == 2:
    print('Knock, knock, {}'.format(sys.argv[1]))
else:
    sys.stderr.write('Usage: {} <name>\n'.format(sys.argv[0]))
