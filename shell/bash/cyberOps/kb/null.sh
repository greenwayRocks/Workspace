#! /bin/sh

a=""
b="not null"

if [[ -z $a && -n $b ]]
then
  echo "met"
else
  echo "not met"
fi
