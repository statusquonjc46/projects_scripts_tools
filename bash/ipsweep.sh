#!/bin/bash
# bash script to ping all IPs on a network by network ID. Learned and Inspired from The Cyber Mentor
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

if [ "$1" == "" ]
then
echo "You forgot to enter a Network address!"
echo "Syntax: ./ipsweep.sh 192.168.1. [For example, 192.168.1 should be replaced with desired network to sweep]"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
