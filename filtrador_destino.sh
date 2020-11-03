#!/usr/bin/env bash
now=$(date +"%d-%m-%y")
grep vuelos | sed '1,6d' | tr '[:lower:]' '[:upper:]' | cut -d '/' -f7 | grep -E '[A-Z]{3}' | cut -d ',' -f1 | sort | uniq -c | sort | awk '{print $1", "$2} ' | header -a Frec.,Dest. | csvlook > Destino_Aereo_$now.txt

