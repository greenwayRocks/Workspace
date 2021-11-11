#! /usr/bin/bash

## Bash Functions To Make Life Easier

# prettyprint on csci-lqa ( some printer I have )

function pretty()
{
  # long syntax that I'm avoiding -------------
  # lpr -P csci-lqa -p $filename -# $num_copies

  if [ $# -eq 0 ] ; then
    echo "Syntax is: pretty filename"
    echo "       or: pretty filename numcopies"
  else
    echo "You typed: $#"
  fi
}

## Verify if functions exist

if declare -f "$1" > /dev/null
then
  "$@"
else
  echo "'$1' is not a known function name!" >&2
  exit 1
fi

## TIP: 2>&1 means all stderr to "stdout" so we can pipe any output
## Note: FD (File Descriptors): 0 -> stdin, 1 -> stdout, 2 -> stderr

## Controversial Truth: $ command > log.txt 2>&1
## Wrong: $ command 2>&1 > log.txt
