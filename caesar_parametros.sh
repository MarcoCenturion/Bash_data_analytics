#!/bin/bash 
# caesar_script
# Aprendiendo a usar tr y pipes
# (c) Marco Centurion

echo "Mensaje secreto"
echo $1 | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
