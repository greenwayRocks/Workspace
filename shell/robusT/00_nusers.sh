#!/bin/bash
# Count the number of login sessions

who | awk '{ print $1 }' | sort | uniq | wc -l
