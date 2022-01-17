#!/usr/bin/env bash

echo "---------------"
echo "Valor Dolar Amadeus"
read dolar1
echo "Fee operador"
read fee1
echo "Fee Uruk"
read fee2
echo "neto operador"
read neto1
echo "--------------"
feepesos=$((dolar1*fee1))
feepesos2=$((dolar1*fee2))
tarifa=$((neto1+feepesos+feepesos2))
echo "Tarifa final al pax: ARS"
echo $tarifa
echo "-------------"

