#!/bin/bash
ipsumfile=/tmp/ipsum.ip

/usr/bin/curl https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt -o $ipsumfile

ipset flush IP_IPSUM

while read ip; do
    ipset add IP_IPSUM "$ip"
done < /tmp/ipsum.ip
