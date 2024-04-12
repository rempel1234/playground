#!/bin/bash
ipsumfile=/tmp/ipsum.ip

/usr/bin/curl https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt -o $ipsumfile
for d in www.facebook.com m.facebook.com facebook.com; do
    dig +short "$d" >> "$fbookfile"
done
sort -n -u "$fbookfile" -o "$fbookfile"
