#!/usr/bin/env bash

# Looping

i=0; j=0

for (( i=0; i<5; i++ ))
do
  for (( j=0; j<5; j++ ))
  do
    printf "#"
  done
done

echo
