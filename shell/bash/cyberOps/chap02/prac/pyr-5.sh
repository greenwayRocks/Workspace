#!/bin/bash -

# regular pyramid - how many ways you can do it?

read -p "enter rows: " rows

# for (( i=1; i<=rows; i++ ))
# do
#   for ((j=1; j<=i; j++))
#   do
#     printf "#"
#   done
#   echo
# done

# some other way? ok!

for (( i=rows; i>=1; i-- ))
do
  for (( j=rows; j>=i; j-- ))
  do
    printf "#"
  done
  echo 
done

# lol took time, thought i couldnot tara ni garesi herda sajilo xa bujhdai janxu ..
