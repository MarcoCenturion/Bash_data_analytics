#!/bin/python3.9

''' Definimos los costos
'''

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
Semanas = [1,2,4]
Years = [1,3,5]

'''Costos'''

SemanaSilver=(CostoNoche*7)*1.33
SemanaGold=(CostoNoche*7)*1.07+(DesayunoNoche*7)
SemanaPlatinum=(CostoNoche*7)+(DesayunoNoche*7)+AlquilerLancha3hs

print("Silver: USD"+str(SemanaSilver)+" ARS"+str(int(SemanaSilver*DolarOficial)))
print("Gold: USD"+str(SemanaGold)+" ARS"+str(int(SemanaGold*DolarOficial)))
print("Platinum: USD"+str(SemanaPlatinum)+" ARS"+str(int(SemanaPlatinum*DolarOficial)))


'''

for i in Years:
    precio=(i*SemanaSilver)
    print("Silver 7 días sin Desayuno ni membresía RCI")
    print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+" = en pesos: ARS"+str(int(precio*DolarOficial))+"\n")
    exit

for i in Years:
    precio=((i*SemanaGold)*2)
    print("Gold 14 días con Desayuno membresía RCI y un paseos en barco por semana")
    print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+" = en pesos: ARS"+str(int(precio*DolarOficial))+"\n")
    exit

for i in Years:
    precio=((i*SemanaPlatinum)*4)
    print("Platinum 28 días con Desayuno, membresía RCI y dos paseos en barco por semana ")
    print("El precio para " +str(i)+" años es Dólares: USD" +str(precio)+" = en pesos: ARS"+str(precio*DolarOficial)+"\n")
    exit'''


Semanas = input("Indicar la cantidad de semanas 1,2,4: ")
Anos = input("Indicar la cantidad de años 1,3,5: ")
# Categoria = input("Indicar categoría Silver, Gold o Platinum: ")
'''
print("Silver 7 días sin Desayuno ni membresía RCI")
print("El precio para " +str(i)+" años es Dólares: USD" +str(int(precio))+" = en pesos: ARS"+str(int(precio*DolarOficial))+"\n")
'''


print('-------------------------\n')
print("La opción elegida es "+str(Semanas)+" Semanas en "+str(Anos)+"\n")
print('-------------------------\n')
precio=((CostoNoche*7)*int(Semanas))*int(Anos)
print("Dolares Total "+str(int(precio))+"\n")
print("Pesos Total "+str(int(precio*DolarBlue))+"\n")
print("12 cuotas de "+str(int((precio*DolarBlue)*1.3)/12)+"\n")
print("24 cuotas de "+str(int((precio*DolarBlue)*1.5)/24)+"\n")
print("36 cuotas de "+str(int((precio*DolarBlue)*1.7)/36)+"\n")