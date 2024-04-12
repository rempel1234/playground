#!/bin/bash

while read line; 
do 
	/usr/sbin/ufw insert 1 deny from $line to any; 
done < /tmp/blacklist
