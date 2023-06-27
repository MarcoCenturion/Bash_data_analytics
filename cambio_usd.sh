#!/bin/bash
# Toma el primer argumento y lo divide por el segundo
# imprime en pantalla el valor

cambio=489

function renglon (){
	printf %80s | tr ' ' '='

}

renglon
echo -e "\nEl importe a cambiar es de ARS"$1
echo -e "El tipo de cambio es"$cambio
echo -e "El importe es USD"$(($1/$cambio))
renglon



