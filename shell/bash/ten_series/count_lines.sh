#!/bin/bash

nlines=`wc -l "$1"`
parsed=`echo $nlines | egrep -o '[0-9]+'`

echo "There are $parsed lines in $1"
