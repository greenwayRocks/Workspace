---
declare -f | grep '^[a-z_]' | less
is equivalent to::
declare -F | awk -F '{ print $3 }' | less
---
