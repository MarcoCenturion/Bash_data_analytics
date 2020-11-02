
fecha='10-2020|11-2020|12-2020'
desti='BRC|IGR|MDQ|FTE|USH|CPC'
cat Analytics\ Vista\ de\ Usuarios\ Vuelos\ por\ agencia\ sin\ DELFOS\ 20201024-20201025.csv | grep -E $desti | grep -E $fecha | sed -n 7,288p | cut -d '/' -f 3,6,7,8 | tr '/' ' ' | csvlook 

