#!/usr/bin/env bash
now=$(date +"%d-%m-%y")
sed '1,6d' | tr '[:lower:]' '[:upper:]' | grep HOTEL | tr '/' ' ' | cut -d ' ' -f3,8,9 > Agy_Htl_Fecha_$now.txt


