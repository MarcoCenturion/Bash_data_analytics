#!/usr/bin/env bash

now=$(date +"%d-%m-%y")
sed '1,6d' | tr '[:lower:]' '[:upper:]' | grep PROD | tr '/' ' ' | cut -d ' ' -f3,7 | cut -d ',' -f1 | cut -d ' ' -f 2 | cut -d '?' -f1 | sort | uniq -c | sort > Paquetes_mas_buscados_$now.txt


