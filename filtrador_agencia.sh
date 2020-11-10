#!/usr/bin/env bash
now=$(date +"%d-%m-%y")
sed '1,6d' | tr '[:lower:]' '[:upper:]' | cut -d '/' -f3 | sort | \
uniq -c | sort | tail | awk '{print $1", "$2}' | header -a Frecuencia.,Agencia. | csvlook > Agencias_$now.txt

