#!/bin/bash 
##########################  LEER_PORTAPAPELES.SH
# leer con xclip el portapapeles
# y pegarlo en una variable
# Grabamos los colores de Savitar
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"
blueColour="\e[0;34m\0m3[1m"
# Establecemos la fecha en la variable now

now=$(date +"%d-%m-%y  %H:%M")
pnr=$(xclip -o)

clear
# Ingresamos el valor del dolar y el Markup
echo -ne "\n${greenColour}Ingresar el valor del dolarblue: ${endColour}" 
read dolarblue
echo -ne "\n${blueColour}------------------------------${endColour}"
echo -ne "\n${greenColour}Esta cotización es del día: $now${endColour}"
echo -ne "\n${greenColour}El valor ingresado es: $dolarbue ${endColour}"
echo -ne "\n${greenColour}Indicar el Markup por tkt: ${endColour}" 
read markup
sleep 1

ltd=$(cat $pnr | grep LAST | awk -F '-' '{print $pnr}')
tarifa_usd=$(cat $pnr | grep USD | awk 'NR == 1 {print $2}')
equipaje=$(cat $pnr | grep -E '2P|1P|0P'|awk '{print $pnr0}')
tramos=$(cat $pnr | grep -e '^  [1-9]'|cut -c 6-12,15-20,23-29,35-43 | awk '{print $0}')
tarifa=$(cat $pnr | grep -e '^ARS' | tail -1 | awk '{print $pnr}' | sed 's/ARS//' | awk -F . '{print $pnr}')

# Imprimimos en pantalla la cotización
echo -e "\n${blueColour}\n----------------------------------${endColour}"
echo -en "\n${blueColour}\nFecha de Cotización Emitida: ${endColour}"
echo -e "${redColour}$now${endColour}"
echo -en "\n${blueColours}Ultimo día para emitir: ${endColour}"
echo -e "${redColour}$ltd${endColour}"
echo -e "${redColour}$tarifa_usd${endColour}"
echo -e "\n${blueColour}Cía|Vuelo|Fecha|Ruta|Sale|Llega${endColour}"
echo -e "${redColour}$tramos${endColour}"
echo -en "\n${blueColour}Equipaje Permitido: ${endColour}"

