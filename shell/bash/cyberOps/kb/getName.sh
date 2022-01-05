#! /bin/bash -

# Get name within 10 seconds
max_time=10

# color codes
reset=$(tput sgr0)
blinkRed=$(tput setab 0; tput setaf 1; tput blink)
cyan=$(tput setab 0; tput setaf 6)

echo $cyan"** You have "$blinkRed"$max_time"$reset$cyan" seconds to type your name!**"$reset


# name within max_time
while (( SECONDS < max_time ))
do
  # rem seconds
  rem_sec=$(( max_time - SECONDS ))

  # prompt for name
  echo -en "\n-["$blinkRed"$rem_sec"$reset"] Enter name: "
  read name

  # empty name
  if [ -z "$name" ]
  then
    echo "Don't mess around!"
  else
    break
  fi
done

# lets see if name is given
if [ -n "$name" ]
then
  echo "Hi, $name!"
else
  echo $cyan"You gave no "$reset$blinkRed"NAME!"$reset
  exit 0
fi

# end
exit 0
echo 'This wont be executed.'
