#! /bin/bash -

user=$(whoami)
date=$(date +"%Y/%m/%d")
time=$(date +"%H:%M:%D")

printf "Current User:\t%s\nDate:\t%s @ %s\n" $user "$date" "$time"
