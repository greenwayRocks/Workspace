#! /bin/sh

# head command implementation in sed

# Usage: head N file

count=$1

sed "${count}q" "$2"
