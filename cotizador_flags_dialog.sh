#!/bin/bash 
#
# Aprendiendo a usar sed, cat, awk, cut
# (c) Marco Centurion
#  Aplicamos while, flag, OPTARG y getops
# -------------------------------------


# Establecemos la fecha en la variable now
now=$(date +"%d-%m-%y  %H:%M")
commia=0.85

while getopts c:m:f:p: flag
do
    case "${flag}" in
        c) cambio=${OPTARG};;
        m) miami=${OPTARG};;
        f) fee=${OPTARG};;
	p) reser=${OPTARG};;
    esac
done

function renglon(){
        printf %50s |tr " " "="
}

# Ingresamos el valor del dolar y el Markup
echo "Esta cotización es del día: $now"
echo "El valor ingresado es: $cambio"
echo "Markup por tkt: $fee" 
echo "PNR leido: $reser"
renglon

# Parseamos el documento txt en cada una de las variables que 
# utilizaremos para hacer la cotización
#
ltd=$(cat $reser | grep LAST | awk -F '-' '{print $1}')
tarifa_usd=$(cat $
reser | grep USD | awk 'NR == 1 {print $2}')
equipaje=$(cat $reser | grep -E '2P|1P|0P'|awk '{print $10}')
tramos=$(cat $reser | grep -e '^  [1-9]'|cut -c 6-12,15-20,23-29,35-43 | awk '{print $0}')
tarifa=$(cat $reser | grep -e '^ARS' | tail -1 | awk '{print $1}' | sed 's/ARS//' | awk -F . '{print $1}')
endos=$(cat $reser | grep -e 'REF')

# Imprimimos en pantalla la cotización
renglon
echo -en "\n\nFecha de Cotización Emitida: "
echo -e "$now"
echo -en "\nUltimo día para emitir: "
echo -e "$ltd"
echo -en "\nImporte en USD sin TAX:  "
echo -e "$tarifa_usd"
echo -e "\nCía|Vuelo|Fecha|Ruta|Sale|Llega"
echo -e "$tramos"
echo -en "\nEquipaje Permitido: \n"
echo -e "$equipaje"
echo -en "\nDevoluciones y cambios: \n"
echo -e "$endos"
echo -en "\nTarifa en Pesos Total por pasajero: ARS "
echo -e "$(($tarifa+$fee))"
echo -en "\nTarifa en Dolares total por pasajero: USD "

#feeusd=((fee/cambio))
#netomia=((miami\*0.85))

echo -en "$((($fee/$cambio)+($miami)))"
