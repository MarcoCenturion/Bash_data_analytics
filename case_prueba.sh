#!/bin/bash
#
# Aprendiendo a usar sed, cat, awk, cut
# (c) Marco Centurion
# -------------------------------------

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

echo "Esta cotización es del día: $now"
echo "El valor ingresado es: $dolarbue"
echo "Markup por tkt" 
read markup

ltd=$(cat pnr.txt | grep LAST | awk -F '-' '{print $1}')
tarifa_usd=$(cat pnr.txt | grep USD | awk 'NR == 1 {print $2}')
equipaje=$(cat pnr.txt | grep -E '2P|1P|0P'|awk '{print $10}')
tramos=$(cat pnr.txt | grep -e '^  [1-9]'|cut -c 6-12,15-20,23-29,35-43 | tr '\n' '\t\t')
tarifa=$(cat pnr.txt | grep -e '^ARS' | tail -1 | awk 'print $1')
clear

echo -e "\n${blueColour}\n----------------------------------${endColour}"
echo -en "\n${blueColour}\nCotización Emitida  ${endColour}"
echo -e ${redColour}$now${endColour}
echo -en "\n${blueColours}Ultimo día para emitir: ${endColour}"
echo -e ${redColour}$ltd${endColour}
echo -en "\n${blueColour}Importe en USD sin TAX:  ${endColour}"
echo -e ${redColour}$tarifa_usd${endColour}
echo -e "\n${blueColour}Cía|Vuelo|Fecha|Ruta|Sale|Llega${endColour}"
echo -e ${redColour}$tramos${endColour}
echo -en "\n${blueColour}Equipaje Permitido :${endColour}"
echo -e ${redColour}$equipaje${endColour}
echo -en "\n${blueColour}Tarifa en Pesos Total por pasajero :${endColour}"
echo -e ${redColour}$tarifa${endColour}
