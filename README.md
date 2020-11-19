# Bash_data_analytics
---
### Scripts para filtrar archivos csv
---
Ejemplos de Comandos de Bash para búsquedas, filtro y presentación de datos de analytics
---

**filtrador_agencia.sh** 
usamos pipes con los comandos tr, cut, sort, uniq tail, awk, header y csvlook

**filtrador_origen.sh** 
a los comandos anteriores agregamos el filtro grep usando expresiones regulares grep -E '[A-Z]{3}' TRES caracters mayusculas de A a Z

**filtrador_hotel_pormes.sh** 
definimos una vairable para el dia de hoy now=$(date +"%d-%m-%y")

**REGEX**
utilizamos la expresion regular de grep para buscar meses puntuales|grep grep -E '(11|12)-2020' y lo escribimos en un archivo puntual tomando la variable para poner el nombre del archivo

**filtro_agencia_vertical.sh**
Primero contamos con wc -l el total de renglones y con el comando sed eliminamos las primeras y las ultimas lineas sed -n '8,155p'

**Filtrador hotel por mes**
Agregamos una expresion regular para buscar un mes o meses grep -E '(11|12)-2020'

**sed para cortar cabecera pie del archivo**
sed -n '7,288p' // corta los primeros 7 renglones y hasta el renglon 288 suponiendo que tiene mas

**awk_archivo**
Es una prueba para agrupar una de las columans

**awk sed tr grep**
- sed secciona los renglones entre 8 y 4124
- tr traduce ? / , y " por un espacio en blanco
- grep selecciona solo los renglones que incluyan la palabra "vuel"
- awk filtra la columna 6 y toma el valor de la comuna 10 para sumarlo
sed -n '8,4124p' | tr '?' ' ' | tr '/' ' ' | tr ',' ' ' | tr ' " ' ' ' | grep vuel | awk '$6=="CUN" { sum += $10 } END { print sum }' 

**script de bash**
shebang
#!/usr/bin/env bash
genera una variable con el día actual
now=$(date +"%d-%m-%y")
toma el resultado que le envia un comando cat a un archivo como entrada
y lo hace pasar por
- grep hotel // solo filtrar hoteles
- sed -n '1,6332d' // muestra solo este rango de renglones 
- tr '[:lower:]' '[:upper:]' // Traduce todas las minúsculas a mayúsculas
- cut -d '/' -f8,9 // corta con el separador / las columnas 8 y 9
- tr '/' ' ' // traduce / por espacio en blaco
- sort // ordena alfabeticamente el resultado
- uniq -c // evalua los únicos y los cuenta
- sort // los ordena una vez contados de menor a mayor -r en orden inverso
- grep -E '(11|12)-2020' // solo los que tengan la expresion regular 11 o 12 del 2020
- > Destino_hotel_pormes_$now.txt // lo escribe en un fichero que toma por nombre la variable $now que asignamos en el primer renglon con el dia de la fecha de sistema.

**usando grep**
grep -E 'BRC|IGR|MDQ|FTE|USH|CPC' // solo alguno de estos destinos
grep -E '10-2020|11-2020' // solo alguna de estas fechas
grep -E '(09|10|11)11-2020' // igual al anterior pero mas simple, tres meses
grep -E '[0-9]{2} [0-9]{2}' // dos dígitos espacio dos dígitos

**awk**
awk -F"/" ' NR==1,NR==10{ print $1, $2, $3 } '

**Contando las busquedas por mes**
cat ~/Descargas/Analytics\ Vista\ de\ Usuarios\ Vuelos\ por\ agencia\ sin\ DELFOS\ 20201117-20201117\(1\).csv | sed '1,6d' | tr '[:lower:]' '[:upper:]' | cut -d '/' -f8 | grep -E '{3,5}' | cut -d '-' -f2 | sort | uniq -c | sort | grep -E '[0-9]{2  } [0-9]{2}' | awk '{print $1", "$2}'                                              
13, 06
21, 05
47, 04
61, 02
61, 11
96, 03
100, 12
125, 01




