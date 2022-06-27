#/!bin/bash
contador=1
cat /etc/passwd | while read line; do
	echo "estamos en $contador $line"
	let contador+=1
done 
