#!/usr/bin/env bash
now=$(date +"%d-%m-%y")
grep hote | sed '1,6d' | tr '[:lower:]' '[:upper:]' | cut -d '/' -f8,9 | tr '/' ' ' | sort | uniq -c | sort | grep -E '(11|12)-2020' > Destino_hotel_pormes_$now.txt

