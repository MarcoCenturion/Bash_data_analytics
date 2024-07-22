#!/usr/bin/python3.12 
# Marco Adrian Centurion (c)
# This script was created by TH Consultora
# to increase capabilities or flight sellers 
# in travel agencies.
# -----------------------------------

# Importamos las bibliotecas a utilizar
import re
import datetime

'''
fee = 0
blue = 0
cabe = input("\n---------------------------------------\nDefinir Cabecera th, ni, gr, pa: ")
cabe = cabe.lower()
fee = int(input("\n-------------------------------------\nDefinir fee en ARS oficial\nPor defecto es ARS46000: "))
blue = int(input("\n-------------------------------------\nIndicar el tipo de cambio blue Vendedor: "))
ventausd = int(input("\n----------------------------------\nIndicar el precio en USD emitiendo en MIA: "))
'''

diccionarios = ['aeropuertos.txt','cabecera.txt','devoluciones.txt','fee_camuflado.txt','financiacion.txt','franquicias.txt','i65promo.txt','i85promo.txt','lineas.txt','mes.txt']

for dic in diccionarios:
    with open(dic,'r') as archivo:
        separador = ':'
        dic = {}
        for linea in archivo:
            key, value = linea.split(separador)
            data[key.strip()] = value.strip()
        print(dic)
