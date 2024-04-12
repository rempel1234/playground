#!/bin/bash
# Place in /etc/cron.daily/getBlacklist

cd /tmp
# get latest black list from abuseIPDB
/usr/bin/touch /tmp/blacklist.txt
/usr/bin/curl -Olk https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt

/usr/bin/sort ipsum.txt > /tmp/blacklist.txt

# Get rid of second colum
/usr/bin/sed -i 's/\t.*//' /tmp/blacklist.txt

# block every ip in list

/usr/local/bin/blacklist.sh

# Shamelessly inspired by https://gist.github.com/MalteKiefer/407849891195a542dfa97329510aa387
