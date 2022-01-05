#! /bin/bash -

# colors
reset=$(tput sgr0)

flashRed=$(tput setab 0; tput setaf 1; tput blink)

cyan=$(tput setab 0; tput setaf 6)

echo $flashRed"Error: "$reset$cyan"Sth went wrong ..."$reset
