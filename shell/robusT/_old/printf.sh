#! /bin/sh -

printf 'Simple output - note the \\n at the end is a newline\n'
read junk

printf 'You cannot use \\c in format strings.'
read junk

printf 'You can use \\c in argument strings: %b - rest ignored\n' 'testing\cnoteforyou here!' 
read junk
printf '\n'

printf 'Enter your name: '
read name
printf 'Nice to meet you, %s.' $name
printf '\n' # echo
