#!/usr/bin/bash -

# Parse CSV files

OLD_IFS="$IFS"; IFS=","

while read product quantity price
do
  echo -e "\t\e[4m\e[1;33m== ${product} ==\e[0m"
  echo -e "\t\e[3mPrice: ${price}\e[0m"
  echo -e "\t\e[3mQuantity: ${quantity}\n\e[0m"
done < "$1"

IFS="$OLD_IFS"
