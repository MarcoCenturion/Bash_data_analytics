#!/usr/bin/env bash
sed '1,6d' | tr '[:lower:]' '[:upper:]' | cut -d '/' -f6 | grep -E '[A-Z]{3}' | cut -d ',' -f1 | sort | uniq -c | sort | awk '{print $1", "$2} ' | header -a Frec.,Orig. | csvlook

