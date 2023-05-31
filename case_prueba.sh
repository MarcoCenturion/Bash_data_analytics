#!/bin/bash
#
#
# 
# Aprendiendo a usar sed, cat, awk, cut
# (c) Marco Centurion
# -------------------------------------

if [[ -f $1 ]]
then
	echo "Leyendo el archivo "$1
	sleep 1 

greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"
blueColour="\e[0;34m\033[1m"

now=$(date +"%d-%m-%y  %H:%M")

clear
echo -ne "\n${greenColour}Ingresar el valor del dolarblue: ${endColour}" 
read dolarblue
echo -ne "\n${blueColour}------------------------------${endColour}"
echo -ne "\n${greenColour}Esta cotización es del día: $now${endColour}"
echo -ne "\n${greenColour}El valor ingresado es: $dolarbue ${endColour}"
echo -ne "\n${greenColour}Indicar el Markup por tkt: ${endColour}" 
read markup

function ruta(){
	cat $1 | grep 
}

ltd=$(cat $1 | grep LAST | awk -F '-' '{print $1}')
tarifa_usd=$(cat $1 | grep USD | awk 'NR == 1 {print $2}')
equipaje=$(cat $1 | grep -E '2P|1P|0P'|awk '{print $10}')
tramos=$(cat $1 | grep -e '^  [1-9]'|cut -c 6-12,15-20,23-29,35-43 | awk '{print $0}')
tarifa=$(cat $1 | grep -e '^ARS' | tail -1 | awk '{print $1}' | sed 's/ARS//' | awk -F . '{print $1}')
clear

echo -e "\n${blueColour}\n----------------------------------${endColour}"
echo -en "\n${blueColour}\nFecha de Cotización Emitida: ${endColour}"
echo -e "${redColour}$now${endColour}"
echo -en "\n${blueColours}Ultimo día para emitir: ${endColour}"
echo -e "${redColour}$ltd${endColour}"
echo -en "\n${blueColour}Importe en USD sin TAX:  ${endColour}"
echo -e "${redColour}$tarifa_usd${endColour}"
echo -e "\n${blueColour}Cía|Vuelo|Fecha|Ruta|Sale|Llega${endColour}"
echo -e "${redColour}$tramos${endColour}"
echo -en "\n${blueColour}Equipaje Permitido: ${endColour}"
echo -e "${redColour}$equipaje${endColour}"
echo -en "\n${blueColour}Tarifa en Pesos Total por pasajero: ARS ${endColour}"
echo -e "${redColour}$(($tarifa+$markup))${endColour}"
echo -en "\n${blueColour}Tarifa en Dolares total por pasajero: USD ${endColour}"
echo -e "${redColour}$((($tarifa+$markup)/$dolarblue))${endColour}"

else
	echo "El archivo" $1 "no fue encontrado"
fi
