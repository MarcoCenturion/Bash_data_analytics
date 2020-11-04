# Bash_data_analytics
Scripts para filtrar archivos csv

Ejemplos de Comandos de Bash para búsquedas, filtro y presentación de datos de analytics


**filtrador_agencia.sh**
usamos pipes con los comandos tr, cut, sort, uniq tail, awk, header y csvlook

**filtrador_origen.sh**
a los comandos anteriores agregamos el filtro grep usando expresiones regulares 
grep -E '[A-Z]{3}' TRES caracters mayusculas de A a Z

**filtrador_hotel_pormes.sh**
definimos una vairable para el dia de hoy
now=$(date +"%d-%m-%y")

utilizamos la expresion regular de grep para buscar meses puntuales
grep grep -E '(11|12)-2020'

y lo escribimos en un archivo puntual tomando la variable para poner el nombre del archivo

**filtro_agencia_vertical.sh**
Primero contamos con wc -l el total de renglones y con el comando sed eliminamos las primeras y las ultimas lineas
sed -n '8,155p'

eliminamos las primera ocho líneas y de 200 las ultimas 5

 
