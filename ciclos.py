miLista = [ i for i in range(100) ]
#Ciclo for

sumaTotal = 0
for x in range(0, len(miLista)):
    print(f"numero = {miLista[x]}")
    sumaTotal += miLista[x]
    print(f"suma Parcial = {sumaTotal}")

print(f"suma total = {sumaTotal}")



# Ciclo while
from random import randint as rng
numeroGanador = 53
numeroActual = miLista[rng(0,100)]
intentos = 1
while numeroActual != numeroGanador:
    print(f"Numero de intentos = {intentos}")
    intentos += 1
    numeroActual = miLista[rng(0,99)]