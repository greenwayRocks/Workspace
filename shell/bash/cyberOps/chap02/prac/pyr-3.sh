#!/usr/bin/env bash

# inverted half-pyramid

read -p 'Enter no of rows: ' rows

i=0; j=0;

for (( i=1; i <=rows; i++ ))
do
  for (( j=rows; j>=i; j-- ))
  do
    printf "#"
  done
  printf "\n"
done
