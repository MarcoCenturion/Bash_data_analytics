Algoritmo ordenar_numeros
	Escribir "Ingresar numero 1"
	leer uno
	Escribir "Ingresar numero 2"
	leer dos 
	Escribir "Ingresar numero 3"
	leer tres
	si uno < dos y dos < tres entonces
		escribir uno
		si dos < tres entonces
			escribir dos 
			escribir tres
		FinSi
	sino 
		si tres < dos 
	FinSi
	
FinAlgoritmo
