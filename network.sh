#!/bin/bash

if [[ "$1" == "eth0" ]]; then
    ip=$(ifconfig eth0 | grep 'inet addr:' | grep Bcast | awk '{print $2}' | awk -F: '{print $2}')
else
    ip=$(ifconfig wlan0 | grep 'inet addr:' | grep Bcast | awk '{print $2}' | awk -F: '{print $2}')
fi

echo $ip
