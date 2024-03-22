#!/bin/bash 
# caesar_script
# Aprendiendo a usar tr y pipes
# (c) Marco Centurion

declare -A aeropuertos
echo "La Concha de tu hermana" | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'

echo "Yn Pbapun qr gh ureznan" | tr '[N-ZA-Mn-za-m]' '[A-Za-z]'
