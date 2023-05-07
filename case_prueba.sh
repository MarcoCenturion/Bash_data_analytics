#!/bin/bash
#
#
# 

greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"
now=$(date +"%d-%m-%y  %m:%S")

echo -ne "\n${greenColour}Ingresar el valor del dolarblue: ${endColour}" 
read dolarblue
echo -e "${blueColour}------------------------------${endColour}"
echo -ne "\n${greenColour}Pegar el PNR: ${endColour}" 
read pnr

echo "Esta cotización es del día: $now"
echo "El valor ingresado es: $dolarbue"

function ruta(){
	cat pnr.txt | grep 
}

