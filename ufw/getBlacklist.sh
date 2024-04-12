#!/bin/bash
# Place in /etc/cron.daily/getBlacklist

# get latest black list from abuseIPDB

curl -G https://api.abuseipdb.com/api/v2/blacklist \
  -d confidenceMinimum=50 \
  -H "Key: <API_KEY>" \
  -H "Accept: text/plain" | sort > /tmp/blacklist

# block every ip in list

/usr/local/bin/blacklist.sh

# Shamelessly inspired by https://gist.github.com/MalteKiefer/407849891195a542dfa97329510aa387
