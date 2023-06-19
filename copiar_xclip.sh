#!/bin/bash
#
# Copia el contenido del portapapeles y lo pega en un archivo
#

pnr=$(xclip -i)

echo $pnr

xclip -o > pnr.txt
