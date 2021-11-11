#! /bin/bash -

 echo 'Simple output with no -n or escapes'
 read junk

 echo -n 'Enter your name: '
 read name
 echo "Nice to meet you, $name."

 read junk

 echo -e 'Please enter yur name again: \c'
 read name
 echo "Don't I know you, $name?"

 read junk

 echo -e 'Please enter your name for the last time: \c other stuff ignored'
 read name
 echo "Well, $name, I have to go now."
 echo
