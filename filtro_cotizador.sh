#!/usr/bin/env bash
now=$(date +"%d-%m-%y")
sed '1,6d' | tr '[:lower:]' '[:upper:]' | grep COTIZA | tr '/' ' ' | cut -d ' ' -f3,7,8 | csvlook > Cotizador_OffLine_$now.txt
