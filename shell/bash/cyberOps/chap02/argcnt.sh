#! /bin/bash -

# count arguments

# display only even ones!@

echo "there are ${#} arguments"

i=1
for arg
do
  if (( i % 2 == 0 ))
  then
    echo "arg${i}: ${arg}"
  fi
  let i++
done
