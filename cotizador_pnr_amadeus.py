# -*- coding: utf-8 -*-
"""Cotizador_PNR_Amadeus.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kPeEAV287t85XNx0u31UHylh3xMTBZlG

# Cotizador Aéreos

## Varios flujos distintos:

- Cabotaje
- Internacional
- Internacional saliendo fuera de Argentina
- Sabre ARS
- Sabre USD

----
"""

# Abrimos el archivo pnr.txt en modo lectura solamente
# lo leemos
# con print nos aseugramos de ver el contenido


print(tst,diccionarios)

"""# Script para cotizar aéreos
## TIPS

- Remarcar la diferencia con Despegar
- Abonando en USD tiene descuento
- Foto de Pasaportes y visa (no tomamos reservas sin esto)
- Equipaje en cabina y en bodega
- Remarcar LTD (ultimo momento para emitir)
- Seguro de Asistencia
- Auto


"""

# Diccionarios a utilizar
# Captura datos
# Importamos la librería RE, definimos un fee por defecto
# y preguntamos al usuario si quiere cambiarlo
import re
import datetime


tst = open('pnr6.txt')
aeropuertos = open('aeropuertos.txt')
cabecera = open('cabecera.txt')


fee = 0
blue = 0
cabe = input("\n---------------------------------------\nDefinir Cabecera th, ni, gr, pa: ")
cabe = cabe.lower()
fee = int(input("\n-------------------------------------\nDefinir fee en ARS oficial\nPor defecto es ARS46000: "))
blue = int(input("\n-------------------------------------\nIndicar el tipo de cambio blue Vendedor: "))
ventausd = int(input("\n----------------------------------\nIndicar el precio en USD emitiendo en MIA: "))

# Desmenuzamos el archivo buscando los campos puntuales con expresiones regulares
pos_carrier=tst.find('CARRIER')
cia=tst[(pos_carrier+8):(pos_carrier+10)]
cambio=re.findall('1USD=(......)', tst)[0]
route = re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{53}',tst, flags=re.M)
orig = re.findall('\n (\w{3})\n', tst)[0]
fare_ars = re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', tst)[0][1]
bagage = re.findall(' (0P|20|30|32|2B|PC|1P|2P|3P)\n', tst)[0]
ltd = re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', tst)[0]
date = re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst)
ttl = re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', tst)[-1][-1]
ref = re.findall('\n(ENDOS|NONREF|NON-REF|NON|TICKETS)', tst)[0]
retenc = re.findall('(\d{0,6}.\d{2})(Q1 |-Q1 )', tst)[0][0]
#fare_usd = re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', tst)[0]

# Los tramos los tomamos del frente del PNR y los recortamos para obtener solo la info relevante
tramo=[]
clases=[]
fechas=[]
contador = len(route)

for renglon in route:
    vuelo = renglon[5:12]
    clase = renglon[12:13]
    fecha = renglon[14:20]
    horarios = renglon[34:44]
    ori = renglon[22:25]
    des = renglon[25:28]
    tramo.append(vuelo+fecha+horarios+aeropuertos.get(ori) + " / " + aeropuertos.get(des))
    fechas.append(fecha)
    clases.append(clase)
    contador = contador-1


# Juntamos toda la info de los tramos
tramos="\n".join(tramo)
clases="".join(clases)

# Agregamos el Fee al total del PNR
total=float(ttl)+float(fee)

ultima=fechas[-1]
primera=fechas[0]

dia_primera = primera[0:2]
mes_primera = primera[2:5]

dia_ultima = ultima[0:2]
mes_ultima = ultima[2:5]

year='-2024 00:00'
inicio = dia_primera+'-'+mes_primera+year
fin = dia_ultima+'-'+mes_ultima+year

dia1 = datetime.datetime.strptime(inicio,'%d-%b-%Y %H:%M')
dia2 = datetime.datetime.strptime(fin,'%d-%b-%Y %H:%M')

dias = (dia2 - dia1) / datetime.timedelta(days=1)

##  Comentar este renglon si no hay cambio de año
#if dias -0:dias=dias+366

##

usd_i65 = i65promo.get(dias)
usd_i85 = i85promo.get(dias)
'''
camuflado = []
largo = len(fee)
for i in fee:
  camuf=fee_camuflado.get(int(i))
  largo = largo+1
  camuflado.append(camuf)
'''
# Escribimos el resultado
texto =(f'{cabecera.get(cabe)}\n--------------------------------------------\nCotización Internacional iniciando vuelos en Argentina \
- NO ES RESERVA\n* Compañia Emisora: {str(lineas.get(cia))}\n* Origen: {str(aeropuertos.get(orig))}\n\n* Despliegue de vuelos en horarios \
 locales\n{str(tramos)}\n\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje \
 incluido: {str(franquicia.get(bagage))}\n* Total con impuestos abonando en pesos argentinos *ARS{str(int(total))}* por pasajero \
 \n* Total con impuestos abonando en billetes dólares estadounidenses CARA GRANDE\n en perfecto estado *USD{str(ventausd+(int(fee/blue)))}* \
 Ahorras USD{str(int(ventausd+(int(fee/blue))-(int(total)/blue)))} \
 \n* Abonando en Pesos solamente importe a recuperar AFIP ARS{str(int(float(retenc)))} \n* Cambios y Devoluciones: {str(devoluciones.get(ref))}\n* Cash o\
 tarjeta de crédito en 1 cuota solamente \n*\n*Recomendamos contratar asistencia al viajero para los {str(int(dias))}\
 días de viaje\n* Cobertura básica i65 ARS{int(float(cambio)*float(usd_i65))}\
 con estas prestarcionaes https://bit.ly/4aUnX3s\n* O la cobertura mayor i85 ARS{int(float(cambio)*float(usd_i85))} con estas \
 prestaciones https://bit.ly/4aSwNPw\n AM-{str(clases)}-{str(fee)}\
 \n* Financiación para Cabotaje {str(str(financiacion.get(cia)))}')

print(texto)

str(int(ventausd+(int(fee/blue))-(int(total)/blue)))

"""# Cotización para Cabotaje"""

# Cabotaje

pos_carrier=tst.find('CARRIER')
cia=tst[(pos_carrier+8):(pos_carrier+10)]
cambio=re.findall('1USD=(......)', tst)
route = re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{53}',tst, flags=re.M)
orig = re.findall('\n (\w{3})\n', tst)[0]
fare_ars = re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', tst)[0][1]
bagage = re.findall(' (0P|20|30|32|2B|PC|1P|2P|3P)\n', tst)[0]
ltd = re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', tst)[0]
date = re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst)
ttl = re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', tst)[-1][-1]
ref = re.findall('\n(ENDOS|NONREF|NON-REF|NON|TICKETS)', tst)[0]
retenc = re.findall('(\d{0,6}.\d{2})(Q1 |-Q1 )', tst)
#fare_usd = re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', tst)[0]

# Los tramos los tomamos del frente del PNR y los recortamos para obtener solo la info relevante
tramo=[]
clases=[]
fechas=[]
contador = len(route)

for renglon in route:
    vuelo = renglon[5:12]
    clase = renglon[12:13]
    fecha = renglon[14:20]
    horarios = renglon[34:44]
    ori = renglon[22:25]
    des = renglon[25:28]
    tramo.append(vuelo+fecha+horarios+aeropuertos.get(ori) + " / " + aeropuertos.get(des))
    fechas.append(fecha)
    clases.append(clase)
    contador = contador-1

# Juntamos toda la info de los tramos
tramos="\n".join(tramo)
clases="".join(clases)

# Agregamos el Fee al total del PNR
total=float(ttl)+float(fee)

ultima=fechas[-1]
primera=fechas[0]

dia_primera = primera[0:2]
mes_primera = primera[2:5]

dia_ultima = ultima[0:2]
mes_ultima = ultima[2:5]

# Escribimos el resultado
texto =(f'{cabecera.get(cabe)}\n--------------------------------------------\nCotización Internacional iniciando vuelos en Argentina - \
NO ES RESERVA\n* Compañia Emisora: {str(lineas.get(cia))}\n* Origen: {str(aeropuertos.get(orig))}\n\n* Despliegue de vuelos en horarios\
 locales\n{str(tramos)}\n\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje \
 incluido: {str(franquicia.get(bagage))}\n**Total con impuestos PAGANDO EN PESOS ARS{str(int(total))} por pasajero* \
 \n* Cambios y Devoluciones: {str(devoluciones.get(ref))}\n* Cash o\
 tarjeta de crédito en 1 cuota solamente \n* Tomamos reserva solo con foto de DNI o \
 Pasaporte\n AM-{str(clases)}-{str(int(fee))}\n* Financiación aqui-> {str(financiacion.get(cia))}')

print(texto)

"""# Area de Pruebas

Probamos armar el cotizador para mascaras en USD
"""

import re
tst = '''
FXZ

01 P1
SELECTED RECOMMENDATION SUCCESSFULLY BOOKED
LAST TKT DTE 14SEP24 - DATE OF ORIGIN
------------------------------------------------------------
     AL FLGT  BK T DATE  TIME  FARE BASIS      NVB  NVA   BG
 TLV
XDXB EK  2451 K  K 14SEP 2355  KLSOSIL1                   2P
 BUE EK   247 K  K 15SEP 0805  KLSOSIL1                   2P

USD   603.00      14SEP24TLV EK X/DXB EK
                  BUE603.00NUC603.00END ROE1.00
USD   224.00YQ    XT USD 10.90F6 USD 1.40ZR
USD    27.75IL
USD    12.30XT
USD   867.05
BAG/SEAT/MEAL/SERVICES AT A CHARGE MAY BE AVAIL.-ENTER FXK
TICKET STOCK RESTRICTION
BG CXR: 2*EK
PRICED WITH VALIDATING CARRIER EK - REPRICE IF DIFFERENT VC
>                                                 PAGE  1/ 2
>
m
PENALTY APPLIES
NON-END/FLEX
>                                                 PAGE  2/ 2
>
rt
--- MSC ---
RP/CORG121MP/
  1  EK2451 K 14SEP 6*TLVDXB DK1  2355 0415  15SEP  E  0 7M8 M
     ADD PASSPORT DTLS IN SSR DOCS CONTACT IN SSR CTCM CTCE
     OPERATED BY FLYDUBAI
     OPERATED BY FLYDUBAI
     SEE RTSVC
  2  EK 247 K 15SEP 7*DXBEZE DK1  0805 2055  15SEP  E  1 77L M
     ADD PASSPORT DTLS IN SSR DOCS CONTACT IN SSR CTCM CTCE
     SEE RTSVC
'''

12# Captura datos
# Importamos la librería RE, definimos un fee por defecto
# y preguntamos al usuario si quiere cambiarlo
import re
import datetime

fee = 46000
blue = 494
cabe = input("\n---------------------------------------\nDefinir Cabecera th, ni, gr, pa: ")
cabe = cabe.lower()
fee = int(input("\n-------------------------------------\nDefinir fee en USD Blue: "))

# Desmenuzamos el archivo buscando los campos puntuales con expresiones regulares

pos_carrier=tst.find('CARRIER')
cia=tst[(pos_carrier+8):(pos_carrier+10)]
route = re.findall(r'^\s{2}\d{1}\s{2}\w{2}.{53}',tst, flags=re.M)
orig = re.findall('\n (\w{3})\n', tst)[0]
bagage = re.findall(' (0P|20|30|32|2B|PC|1P|2P|3P)\n', tst)[0]
ltd = re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', tst)[0]
date = re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst)
ttl = re.findall('\nUSD(\D{0,3}\d{1,6}.\d{2})', tst)[-1]
ref = re.findall('\n(ENDOS|NONREF|NON-REF|NON|NON-REF|NONEND)', tst)[0]
# retenc = re.findall('(\d{0,6}.\d{2})(Q1 |-Q1 )', tst)
# fare_usd = re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', tst)[0]

# Los tramos los tomamos del frente del PNR y los recortamos para obtener solo la info relevante
tramo=[]
clases=[]
fechas=[]
contador = len(route)

for renglon in route:
    vuelo = renglon[5:12]
    clase = renglon[12:13]
    fecha = renglon[14:20]
    horarios = renglon[34:44]
    ori = renglon[22:25]
    des = renglon[25:28]
    tramo.append(vuelo+fecha+horarios+aeropuertos.get(ori) + " / " + aeropuertos.get(des))
    fechas.append(fecha)
    clases.append(clase)
    contador = contador-1

# Juntamos toda la info de los tramos
tramos="\n".join(tramo)
clases="".join(clases)

# Agregamos el Fee al total del PNR
total=float(ttl)+float(fee)

ultima=fechas[-1]
primera=fechas[0]

dia_primera = primera[0:2]
mes_primera = primera[2:5]

dia_ultima = ultima[0:2]
mes_ultima = ultima[2:5]

year='-2024 00:00'
inicio = dia_primera+'-'+mes_primera+year
fin = dia_ultima+'-'+mes_ultima+year

dia1 = datetime.datetime.strptime(inicio,'%d-%b-%Y %H:%M')
dia2 = datetime.datetime.strptime(fin,'%d-%b-%Y %H:%M')

dias = (dia2 - dia1) / datetime.timedelta(days=1)

##  Comentar este renglon si no hay cambio de año
#if dias -0:dias=dias+366

##

usd_i65 = i65promo.get(dias)
usd_i85 = i85promo.get(dias)
'''
camuflado = []
largo = len(fee)
for i in fee:
  camuf=fee_camuflado.get(int(i))
  largo = largo+1
  camuflado.append(camuf)
'''
# Escribimos el resultado
texto =(f'{cabecera.get(cabe)}\nCotización Internacional iniciando\
 vuelos en Argentina *NO ES RESERVA*\n* Compañia Emisora: {str(lineas.get(cia))}\n* Origen: {str(aeropuertos.get(orig))}\
 \n\n* Despliegue de vuelos en horarios locales\n{str(tramos)}\n\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje \
 incluido: {str(franquicia.get(bagage))}\n* Cambios y Devoluciones: {str(devoluciones.get(ref))}\n* Cash o \
 tarjeta de crédito en 1 cuota solamente\n**Emitiendo en billetes dólares físicos IMPECABLES cara\
 grande USD {str(int(total))}*\n* Tomamos reserva solo con foto de DNI -Cabotaje- o Pasaporte -Internacional-\
 Pasaporte\n--------------------------------------------\n*Recomendamos contratar asistencia al viajero para los {str(int(dias))}\
 días de viaje\n* Cobertura básica i65 USD{str(usd_i65)}\
 con estas prestarcionaes https://bit.ly/4aUnX3s\n* O la cobertura mayor i85 USD{str(usd_i85)} con estas \
 prestaciones https://bit.ly/4aSwNPw\n AM-{str(clases)}-{str(fee)}\
 \n* Financiación para Cabotaje {str(str(financiacion.get(cia)))}')

print(texto)

"""Sabre USD"""

tst = '''
WPNC¥MUSD5FEB Departure Date-----Last Day to Purchase 31MAY/12:03Base FareTaxes/Fees/Charges1-USD363.00USD535.60XTUSD898.60ADTXT52.00AR57.00XR8.00TQ10.00QO0.00YQ22.10JD3.QV0.70OG2.00S7363.00535.60Total:USD898.60


ADT-1ELRTZ2EBANRSZ1EBCOR AR X/BUE AR MAD227.50AR X/BUE AR COR135.00NUC362.50END ROE1.00NONEND/NONREFVALIDATING CARRIER - ARCAT 15 SALES RESTRICTIONS FREE TEXT FOUND - VERIFY RULES
*I
 1 AR1551E 25FEB T CORAEP*SS1   725A  845A /DCAR /E
 2 AR1134E 25FEB T EZEMAD*SS1   140P  555A  26FEB W /DCAR /E
 3 AR1135A 29MAR J MADEZE*SS1   830A  540P /DCAR /E
 4 AR1552G 29MAR J AEPCOR*SS1  1000P 1130P /DCAR /E
'''

# Desmenuzamos el archivo buscando los campos puntuales con expresiones regulares

pos_carrier=tst.find('CARRIER')
cia=tst[(pos_carrier+10):(pos_carrier+12)]
# cambio=re.findall('1USD=(......)', tst)
route = re.findall(r'^ . \w{2}\d{2,4}\w{1} \d{2}\w{3}...\w{6}.\w{3}\D{2,3}\w{4,5}\D{1,2}\w{4,5}',tst,flags=re.M)
# orig = re.findall('\n (\w{3})\n', tst)[0]
# fare_ars = re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', tst)[0][1]
# bagage = re.findall(' (0P|20|30|32|2B|PC|1P|2P|3P)\n', tst)[0]
ltd = re.findall(r'\d{2}\D{3}\/\d{2}:\d{2}', tst)[0]
# date = re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', tst)
ttl = re.findall('Total:USD\d{1,4}', tst)[-1][9:]
# ref = re.findall('\n(ENDOS|NONREF|NON-REF|NON|TICKETS|NONEND)', tst)
# retenc = re.findall('(\d{0,6}.\d{2})(Q1 |-Q1 )', tst)
#fare_usd = re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', tst)[0]

# Los tramos los tomamos del frente del PNR y los recortamos para obtener solo la info relevante
tramo=[]
clases=[]
fechas=[]
contador = len(route)

for renglon in route:
    vuelo = renglon[3:9]
    clase = renglon[9:10]
    fecha = renglon[11:16]
    ori = renglon[19:22]
    des = renglon[22:25]
    horarios = renglon[31:42]
    tramo.append(vuelo+' '+fecha+' '+horarios+' '+aeropuertos.get(ori) + " / " + aeropuertos.get(des))
    fechas.append(fecha)
    clases.append(clase)
    contador = contador-1

# Juntamos toda la info de los tramos
tramos="\n".join(tramo)
clases="".join(clases)

# Agregamos el Fee al total del PNR
total=float(ttl)+float(fee)


# Escribimos el resultado
texto =(f'{cabecera.get(cabe)}\nCotización Internacional iniciando\vuelos en Argentina *NO ES RESERVA*\n* Compañia Emisora: {lineas.get(cia)}\
\n\n* Despliegue de vuelos en horarios locales\n{str(tramos)}\n\n* Ultimo día para emitir: {str(ltd)}\
\n* Cash o tarjeta de crédito en 1 cuota solamente\n**Emitiendo en billetes dólares físicos IMPECABLES cara \
grande USD {str(int(total))}*\n* Tomamos reserva solo con foto de DNI -Cabotaje- o Pasaporte -Internacional-\
 Pasaporte ')

print(texto)

pos_carrier=tst.find('CARRIER')
cia=tst[(pos_carrier+10):(pos_carrier+12)]
type(cia)

horarios = renglon[31:42]
horarios

ref = re.findall('\n(ENDOS|NONREF|NON-REF|NON|TICKETS|NONEND)', tst)
ref

ttl = re.findall('Total:USD\d{1,4}', tst)[-1][9:]
ttl

route = re.findall(r'^ . \w{2}\d{2,4}\w{1} \d{2}\w{3}...\w{6}.\w{3}\D{2,3}\w{4,5}\D{1,2}\w{4,5}',tst,flags=re.M)
print(route)

ltd = re.findall(r'\d{2}\D{3}\/\d{2}:\d{2}', tst)[0]
print(ltd)
