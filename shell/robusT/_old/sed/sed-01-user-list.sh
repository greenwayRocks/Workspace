#! /bin/sh

grep '/home/' /etc/passwd | # Find real users
          sed 's/:.*//' | # Remove everything after user name
                sort -u | # Sort the list
