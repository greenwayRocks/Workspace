#! /bin/bash -

# Using $seconds to make a 30-sec script

while (( SECONDS < 10 ))
do
  rem_sec=$(( 10 - $SECONDS ))
  read -p "..[-$rem_sec] Enter your name: " name
  echo $name
done

exit 0

echo this wont be displayed, script exited
