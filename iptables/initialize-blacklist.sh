#!/bin/bash

# intialize/allocate the blacklist
ipset create IP_IPSUM hash:ip hashsize 1024

iptables -t raw -A PREROUTING -m set --match-set IP_IPSUM src -j LOG --log-prefix "IPSUM:DROP:" --log-level 6
iptables -t raw -A PREROUTING -m set --match-set IP_IPSUM src -j DROP
iptables -t raw -A PREROUTING -m set --match-set IP_IPSUM dest -j LOG --log-prefix "IPSUM:DROP:" --log-level 6
iptables -t raw -A PREROUTING -m set --match-set IP_IPSUM dest -j DROP
