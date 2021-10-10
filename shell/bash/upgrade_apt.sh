#!/usr/bin/env bash

echo 'Upgrading all apt upgrades to the fullest...'

list=`sudo apt list --upgradable | grep -iv 'LisTiNg' | cut -d '/' -f 1`
echo $list

for i in $list; \
    do sudo apt install -y ${i}; \
    done

echo 'Done!!!'
