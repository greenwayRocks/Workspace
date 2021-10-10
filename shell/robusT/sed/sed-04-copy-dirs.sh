#! /bin/sh

user=$1
find "/home/${user}" -type d -print 2> /dev/null |
    sed "s;/home/${user};&-back;" |
        sed 's/^/mkdir /'
