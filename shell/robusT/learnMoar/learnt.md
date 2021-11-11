awk 'NR == 1; NR > 1 { print ($2=="F" ? ($1-32)/1.8 : $1)" C"; }' temps.csv
