import sys

CostoNoche = 80
DesayunoNoche = 14 
PaseoVelero = 20
DolarOficial = 95
DolarBlue = 140
AlquilerVelero6hs = 50
AlquilerLancha3hs = 50
ExpensasXSemana = 245
IntercambioNacional = 240
IntercambioInternacional = 369
Semanas = [1,2,3,4]
Years = [1,3,5]

for i in Years:
    for t in Semanas:
            precio=(i*(CostoNoche)*7)*t
            print("Y"+str(int(i))+"W"+str(int(t))+" | \tUSD "
                +str(int(precio))+"\tARS "+str(int(precio*DolarBlue))+"\t"
                +"| Anticipo 25% ARS "+str((int(precio*DolarBlue)*.25))
                +" + 12 c ARS "+str((int(precio*DolarBlue)*.75)/12))
            print('\n')
    exit
exit

print("\n------------------\nCon un costo por noche de USD"
    +str(CostoNoche)+"\nExpensas de USD35 por noche total por noche ARS"
    +str(int(35*DolarBlue)+(CostoNoche)*DolarBlue))


'''
for i in Years:
    for t in Semanas:
        precio=(i*Gol)*t
        print("Gold "+str(int(t))+" Semanas c/Desay + RCI + 15 off gastronomia")
        print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+
            " = en pesos: ARS"+str(int(precio*DolarBlue))+"\n")
    exit
exit

for i in Years:
    for t in Semanas:
        precio=(i*Pla)*t
        print("Platinum "+str(int(t))+" Semanas C/des + RCI + Velero + Lancha + 30 off gastronomia")
        print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+
            " = en pesos: ARS"+str(int(precio*DolarBlue))+"\n")
    exit
exit'''
