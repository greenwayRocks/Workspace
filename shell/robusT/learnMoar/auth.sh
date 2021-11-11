#! /bin/bash -

FILE="/etc/shadow"

# Prompt username and password
read -p 'Enter username: ' USER_NAME
read -sp 'Enter password: ' USER_PWD
echo

# Original Password
PWD=$(awk -F: -v pattern="$USER_NAME" '$0 ~ pattern { print $2 }' $FILE)

# My_WAY ------------------------------------------------------
# PWD=$(sudo getent shadow $USER_NAME | awk -F: '{ print $2 }')

IFS='$' read -a PWD_ARRAY <<< "$PWD"

# Entered Password
ENT_PWD=$(openssl passwd -${PWD_ARRAY[1]} -salt ${PWD_ARRAY[2]} ${USER_PWD})

## Authenticate !!

if [ "$PWD" == "$ENT_PWD" ] ; then
  echo "Auth"
else
  echo "NoAuth"
fi
