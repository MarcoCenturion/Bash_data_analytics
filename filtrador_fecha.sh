#!/usr/bin/env bash

now=$(date +"%d-%m-%y")
sed '1,6d' | tr '[:lower:]' '[:upper:]' | cut -d '/' -f8 | grep -E '{3,5}' | cut -d '-' -f2 \
| sort | uniq -c | sort | grep -E '[0-9]{2} [0-9]{2}' | awk '{print $1", "$2}' | header -a Freq,Mes | csvlook > Mes_$now.txt

