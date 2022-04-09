#!/bin/bash

#echo "cual es tu nombre"
#read nombre
#echo "Hola $nombre"

opciones="Saludar Revisar Funcion Salir"

function funcion {
	echo "hola desde la función"
	}
echo "selecciona una de las opciones :)"
clear 


select opcion in $opciones;

do
	if [ $opcion = "Saludar" ]; then
		echo "hola usuario"
	elif  [ $opcion = "Revisar" ]; then
		ls -lsa
	elif [ $opcion = "Funcion" ]; then
		funcion	
	elif [ $opcion = "Salir" ];then
		echo "by"
		exit
	else	
		echo "no esta permitido lo que hiciste"
	fi	
done
