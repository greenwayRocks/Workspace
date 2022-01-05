#! /bin/sh

time_taken=$(ping -c 1 8.8.8.8 | grep -i "bytes from" | cut -d"=" -f4)

echo "It took $time_taken seconds."
