#!/bin/bash -

# check if a certain user exists

read -p 'Enter a user name: ' user

# what to do with the user name? Check if it exists

[[ -d /home/${user} ]] && echo 'yes, the user exists' || echo "nope, ${user} is not a user in this machine!"

# enquiring into a life where there's no "image", no "conflict"
