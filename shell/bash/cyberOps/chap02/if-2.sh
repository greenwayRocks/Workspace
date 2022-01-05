#!/bin/bash -

read -p "Enter a possible file: " FILENAME

if [[ -e $FILENAME ]]
then
  echo "$FILENAME exists!"
else
  echo "$FILENAME doesnot exist!"
fi
