#!/bin/bash -

# inverted pyramid - the other way!

read -p 'Enter no of rows: ' rows

for (( i=rows; i>=1; i-- ))
do
  for (( j=1; j<=i; j++ ))
  do
    printf "#"
  done
  printf "\n"
done

