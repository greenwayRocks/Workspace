#! /bin/bash -
# echo simple without using -ne (newline and escape chars)
# auto new line unless '-n'

echo Simple output with nth -n -e switches    but is this space there?
read junk # -----

echo -n 'Enter your name: '
read name
echo "Nice   - to meet you, $name;"

read junk # -----

echo -e 'Enter it again!: \c'
read name
echo "Don't I know you, $name"

read junk # -----

echo -e 'This gets echoed\c but what about this?'
read junk
echo "Well, I'll have to go now, $name"
