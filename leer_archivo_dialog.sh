#!/bin/bash -x
#
# Leemos un archivo con dialog
#
# (c) Marco Centurion
#

respuesta=$(dialog --backtitle "www.thconsultora.com.ar" \
	--title "Seleccionar un archivo con el pnr a leer" \
	--stdout \
	--fselect $HOME/ 0 0 )

if [ -f "$respuesta" ]
then
	dialog --title "Leer archivo" \
		--yesno "¿Seguro que leemos este archivo? ${respuesta}" 0 0 
	ans=$?
	if [ $ans -eq 0 ]
	then
		pnr=$respuesta
		dialog --msgbox "Archivo leido" \
			--textbox $respuesta
		
