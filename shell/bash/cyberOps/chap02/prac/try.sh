#!/usr/bin/env bash

# inverted pyramid trying some other way

read -p "Enter rows: " rows

for (( i=1; i<=rows; i++ ))
do
  for (( j=rows; j>=i; j-- ))
  do
    printf "#"
  done
  echo
done
