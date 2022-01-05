#!/bin/bash -

# half pyramid of numbers

m=0; n=0;

read -p "Enter no. of rows: " rows

for (( m=1; m <= rows; m++ ))
do
  for (( n=1; n <= m; n++ ))
  do
    echo -n "${n}"
  done
  printf "\n"
done
