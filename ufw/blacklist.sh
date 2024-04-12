#!/bin/bash
# Block both ways
while read line; 
do 
	/usr/sbin/ufw prepend deny from $line to any;
	/usr/sbin/ufw prepend deny from any to $line; 
done < /tmp/blacklist.txt
