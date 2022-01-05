#!/usr/bin/bash -

# 1st pyramid

x=0; y=0;

read -p "Enter no. of rows: " rows

for (( x=1; x <= rows; x++ ))
do
  for (( y=1; y <= x; y++ ))
  do
    printf "#"
  done
  printf "\n"
done
