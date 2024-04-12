#!/bin/bash

while read line; 
do 
	/usr/sbin/ufw prepend deny from $line to any; 
done < /tmp/blacklist.txt
