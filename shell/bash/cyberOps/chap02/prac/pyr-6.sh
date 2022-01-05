#!/usr/bin/bash -

# finally an attempt to make a full pyramid

read -p 'Enter no of rows: ' rows

for (( i=1; i <= rows; i++ ))
do
  # spaces
  for (( j=1; j <= (rows-i); j++ ))
  do
    printf " "
  done
  
  # stars
  for (( k=1; k <= i; k++ ))
  do
    printf "*"
  done

  # newline
  printf "\n"

done
  
