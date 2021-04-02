import sys

CostoNoche = 33
DesayunoNoche = 14 
PaseoVelero = 20
DolarOficial = 95
DolarBlue = 141
AlquilerVelero6hs = 50
AlquilerLancha3hs = 50
ExpensasXSemana = 245
IntercambioNacional = 240
IntercambioInternacional = 369
Categorias = ['silver','gold','platinum']
Semanas = [1,2,3,4]
Years = [1,3,5]

## Costos

SemanaSilver=(CostoNoche*7)*1.33
SemanaGold=(CostoNoche*7)*1.07+(DesayunoNoche*7)
SemanaPlatinum=(CostoNoche*7)+(DesayunoNoche*7)+AlquilerLancha3hs

print("Silver: USD"+str(SemanaSilver)+" ARS"+str(int(SemanaSilver*DolarBlue)))
print("Gold: USD"+str(SemanaGold)+" ARS"+str(int(SemanaGold*DolarBlue)))
print("Platinum: USD"+str(SemanaPlatinum)+" ARS"+str(int(SemanaPlatinum*DolarBlue)))


for i in Years:
    for t in Semanas:
        precio=(i*SemanaSilver)*t
        print("Silver "+str(int(t))+" Semanas s/des ni RCI")
        print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+
            " = en pesos: ARS"+str(int(precio*DolarBlue))+"\n")
    exit
exit

for i in Years:
    for t in Semanas:
        precio=(i*SemanaGold)*t
        print("Gold "+str(int(t))+" Semanas c/Desay + RCI + 15 off gastronomia")
        print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+
            " = en pesos: ARS"+str(int(precio*DolarBlue))+"\n")
    exit
exit

for i in Years:
    for t in Semanas:
        precio=(i*SemanaPlatinum)*t
        print("Platinum "+str(int(t))+" Semanas C/des + RCI + Velero + Lancha + 30 off gastronomia")
        print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+
            " = en pesos: ARS"+str(int(precio*DolarBlue))+"\n")
    exit
exit