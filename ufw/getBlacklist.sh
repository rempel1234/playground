#!/bin/bash
# Place in /etc/cron.daily/getBlacklist

# get latest black list from abuseIPDB

curl -Ol https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt | sort > /tmp/blacklist

# block every ip in list

/usr/local/bin/blacklist.sh

# Shamelessly inspired by https://gist.github.com/MalteKiefer/407849891195a542dfa97329510aa387
