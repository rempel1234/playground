#!/bin/bash
ipsumfile=/tmp/ipsum.ip
for d in www.facebook.com m.facebook.com facebook.com; do
    dig +short "$d" >> "$fbookfile"
done
sort -n -u "$fbookfile" -o "$fbookfile"
