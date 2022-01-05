#!/bin/bash -

# if in action

read -p "Enter a directory: " my_dir

if cd $my_dir
then
  echo "Here is what's in /var/tmp: "
  ls -l --color=auto
else
  echo "No directory called: ${mydir} found!"
fi
