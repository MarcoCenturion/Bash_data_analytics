#!/bin/env bash
# Filtrador para busquedas en analytics usando AWK
awk -F"/" ' NR==1,NR==10{ print $1, $2, $3 } ' 
