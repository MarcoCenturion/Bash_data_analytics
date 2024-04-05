# Diccionarios a utilizar

aeropuertos = {
    "ADD": "Addis Ababa, Ethiopia",
    "ADZ": "San Andrés",
    "AEP": "Aeroparque, Buenos Aires",
    "AKL": "Auckland, New Zeland",
    "ALC": "Alicante",
    "AMS": "Amsterdam, Países Bajos",
    "ASU": "Asunción, Paraguay",
    "ATH": "Atenas, Grecia",
    "ATL": "Atlanta, USA",
    "AUA": "Aruba",
    "AVV": "Melbourne, Australia",
    "BHI": "Bahia Blanca",
    "BCN": "Barcelona",
    "BOG": "Bogotá",
    "BRC": "San Carlos de Bariloche",
    "BUE": "Buenos Aires",
    "CDG": "Charles De Gaulle, París",
    "CGH": "Congonhas, Sao Paulo",
    "CJC": "Calama, Chile",
    "COR": "Córdoba",
    "CPC": "San Martín de los Andes",
    "CTG": "Cartagena de Indias",
    "CUN": "Cancún",
    "CUR": "Curazao, Antillas Holandesas",
    "CUZ": "Cuzco",
    "EWR": "Newark New York",
    "EZE": "Ezeiza, Buenos Aires",
    "FCO": "Fiumicino, Roma",
    "FLN": "Florianópolis",
    "FRA": "Frankfurt",
    "FTE": "El Calafate",
    "GIG": "El Galeao, Rìo de Janeiro",
    "GLA": "Glasgow, Escocia",
    "GRU": "Guarulhos, Sao Paulo",
    "GUA": "Ciudad de Guatemala",
    "GYE": "Guayaquil, Ecuador",
    "HAV": "La Habana, Cuba",
    "HOU": "Houston, Texas",
    "IAH": "Houston, Texas, USA",
    "IGR": "Puerto Iguazú, Argentina",
    "IGU": "Foz do Iguazu, BR",
    "IQQ": "Iquique, Chile",
    "IST": "Istambul, Turkey",
    "JFK": "John F. Kenedy New York",
    "JUJ": "Jujuy",
    "LAP": "La Paz, Mexico",
    "LAS": "Las Vegas",
    "LAX": "Los Angeles, California",
    "LGA": "La Guardia New York",
    "LGW": "London",
    "LHR": "Heathrow, London",
    "LIM": "Lima, Perú",
    "LIS": "Lisboa",
    "MAD": "Madrid",
    "MCO": "Orlando, Florida, US",
    "MDZ": "Mendoza",
    "MDQ": "Mar del Plata",
    "MEC": "Manta, Ecuador",
    "MEL": "Melbourne, Australia",
    "MEX": "México DF",
    "MIA": "Miami, USA",
    "MIL": "Milano",
    "MXP": "Malpensa, Milano",
    "NLU": "Felipe Angeles, Mexico DF",
    "ORD": "Chicago, USA",
    "ORY": "Orly, París",
    "POA": "Porto Allegre",
    "PMI": "Palma de Mallorca, Islas Baleares, España",
    "PTY": "Panamá",
    "ROS": "Rosario",
    "PUJ": "Punta Cana",
    "RDD": "Readding, California",
    "SCL": "Santiago de Chile",
    "SDQ": "Santo Domingo, Repùblica Dominicana",
    "SDU": "Santos Dumont Rio de Janeiro",
    "SFO": "San Francisco, California",
    "SJD": "Los Cabos, Mexico",
    "SLA": "Salta",
    "SMR": "Santa Marta, Colombia",
    "SSA": "Salvador, Bahia",
    "SVQ": "Sevilla",
    "SYD": "Sydney",
    "TIJ": "Tijuana, Mexico",
    "UIO": "Quito, Ecuador",
    "USH": "Ushuaia",
    "VLC": "Valencia, España",
    "VVI": "Santa Cruz de la Sierra, Bolivia"
}

lineas = {
    "AR": "Aerolíneas Argentinas",
    "CM": "Copa Airlines",
    "LA": "Latam",
    "KL": "KLM, Royal Dutch Airlines",
    "AA": "American Airlines",
    "DL": "Delta Airlines",
    "UX": "Air Europa",
    "IB": "Iberia",
    "AF": "Air France",
    "UA": "United Airlines",
    "G3": "Gol Lihnas Aereas",
    "WJ": "Jet Smart",
    "OB": "Boliviana de Aviación",
    "H2": "Sky Airlines",
    "ET": "Ethiopian Airlines",
    "JA": "Jetsmart Spa"
}

# 0P|20|30|32|2B|PC|1P|2P|3P
franquicia = {
    "0P": "Solo 1 carryon de 10 kg. en cabina, sin equipaje en bodega",
    "1P": "Carryon de 10 kg. en cabina + una maleta despachada en bodega de 23kg",
    "2P": "Carryon de 10 kg. en cabina + dos maletas despachadas en bodega de 23kg c/u",
    "30": "Carryon de 10 kg. en cabina + una maleta despachada en bodega de 30kg",
    "3P": "Carryon de 10 kg. en cabina + tres maletas despachadas en bodega de 23kg c/u"
}

devoluciones = {
    "NON-REF": "No permite devoluciones ni cambios",
    "NON-END": "No permite devoluciones ni cambios"
}

financiacion = {
    "AR": "https://www.aerolineas.com.ar/es-ar/reservasservicios/bancos",
    "WJ":"https://jetsmart.com/ar/es/minisitios/medios-de-pago"
}

cabecera = {
    "th": "\n*TURISMO Y HOTELERÍA CONSULTORA*\nwww.thconsultora.com.ar | email: marco@thconsultora.com.ar |\
 Tel/Wp: +543513070654",
    "gr": "\n*GRIFFIN VIAJES* | Leg. 10659 | San Jeronimo 167 Local 16 Gal. Saint Michell\nwww.griffinviajes.com.ar | email: aulavirtualturismo.com.ar |\
 cel/Wp: +543513070654 | Tel: +543514245547 ",
    "pa":"\n*Pampero Viajes y Turismo | EVT Leg 18042* | \nAviador Richardson 2150 1ºA - Córdoba | Tel: 3515190438 | Mail: pamperoviajesyturismo@gmail.com",
    "ni":"\n*TRIBU TRAVEL TOUR* | Leg. 18163 \nhttps://tribu-travel-tour.misitiosimple.com/\nAvellaneda 534 Alta Gracia | Tel/Wp:3513019736"
}


# Captura datos
# Importamos la librería RE, definimos un fee por defecto
# y preguntamos al usuario si quiere cambiarlo
import re
fee = 46000
blue = 494
cabe = input("\n---------------------------------------\nDefinir Cabecera th, ni, gr, pa: ")
cabe = cabe.lower()
fee = int(input("\n-------------------------------------\nDefinir fee en ARS oficial\nPor defecto es ARS46000: "))
blue = int(input("\n-------------------------------------\nIndicar el tipo de cambio blue Vendedor: "))
ventausd = int(input("\n----------------------------------\nIndicar el precio en USD emitiendo en MIA: "))

# Abrimos el archivo pnr.txt en modo lectura solamente
# lo leemos
# con print nos aseugramos de ver el contenido

tst = '''
FXR

01 P1
NO REBOOKING REQUIRED FOR LOWEST AVAILABLE FARE
LAST TKT DTE 18APR24 - DATE OF ORIGIN
------------------------------------------------------------
     AL FLGT  BK T DATE  TIME  FARE BASIS      NVB  NVA   BG
 COR
 RIO G3  7613 N  N 18APR 0400  NNFCAG2G        18APR18APR 0P
 COR G3  7612 E  E 29APR 2230  ENACAG2G        29APR29APR 0P

USD   507.00      18APR24COR G3 RIO203.00G3 COR304.00NUC
ARS444132.00      507.00END ROE1.00
ARS 31089.20-AR   XT ARS 133239.60-Q1 ARS 8760.00-QO ARS
ARS133239.60-O5   1226.40-S7 ARS 7008.00-TQ ARS 49932.00-XR
ARS209608.70-XT   ARS 9442.70-BR
ARS818069.50
RATE USED 1USD=876.00ARS
NO BAG INCLUDED FOR AT LEAST ONE FLIGHT
FARE FAMILIES:    (ENTER FQFn FOR DETAILS, FXY FOR UPSELL)
FARE FAMILY:FC1:1:LT
>                                                 PAGE  2/ 3
>
m
FARE FAMILY:FC2:2:LT
FXU/TS TO UPSELL PL-LT FOR 51202.20ARS
TICKET STOCK RESTRICTION
BG CXR: G3/G3
PRICED WITH VALIDATING CARRIER G3 - REPRICE IF DIFFERENT VC
TICKETS ARE NON-REFUNDABLE
ENDOS NONEND/NONTRANS/
>                                                 PAGE  3/ 3
>
rt
RP/CORG121MP/
  1  G37613 N 18APR 4 CORGIG DK1  0400 0705  18APR  E  0 738 M
     010 AA 7695 /AR 7742 /KL 9383
     SEE RTSVC
  2  G37612 E 29APR 1 GIGCOR DK1  2230 0220  30APR  E  0 738 M
     010 AA 7727 /AR 7743 /KL 9372
     SEE RTSVC
'''

print(tst)

# Desmenuzamos el archivo buscando los campos puntuales con expresiones regulares

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
contador = len(route)

for renglon in route:
    vuelo = renglon[5:12]
    clase = renglon[12:13]
    fecha = renglon[14:20]
    horarios = renglon[34:44]
    #orides = renglon[22:29]
    ori = renglon[22:25]
    des = renglon[25:28]
    tramo.append(vuelo+fecha+aeropuertos.get(ori) + " / " + aeropuertos.get(des)+" "+horarios)
    clases.append(clase)
    contador = contador-1

# Juntamos toda la info de los tramos
tramos="\n".join(tramo)
clases="".join(clases)

# Agregamos el Fee al total del PNR
total=float(ttl)+float(fee)

totalblue = float(total) / float(blue)
totalmia = (float(fee) / float(blue)) + float(((ventausd)*.999)+5)

# Escribimos el resultado
texto =(f'{cabecera.get(cabe)}\n--------------------------------------------\nCotización Internacional iniciando vuelos en Argentina - NO ES RESERVA\n* Compañia \
 Emisora: {str(lineas.get(cia))}\n* Origen: {str(aeropuertos.get(orig))}\n\n* Despliegue de vuelos en horarios\
 locales\n{str(tramos)}\n\n* Ultimo día para emitir: {str(ltd)}\n* Equipaje \
 incluido: {str(franquicia.get(bagage))}\n**Total con impuestos PAGANDO EN PESOS ARS: {str(total)} por pasajero*\n* Cambios y Devoluciones: {str(devoluciones.get(ref))}\n* Cash o\
 tarjeta de crédito en 1 cuota solamente\n**Emitiendo en dólares físicos IMPECABLES cara \
 grande USD {str(int(totalmia))}* / Ahorras USD{str(int(totalblue)-int(totalmia))} emitiendo en Dólares*\n* Tomamos reserva solo con foto de DNI o \
 Pasaporte\n* Recomendamos llevar asistencia al viajero ver opciones aqui -> https://www.thconsultora.com.ar/shop \n {str(clases)}{str(int(fee/blue))}')

print(texto)
