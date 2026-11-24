#Opcion 1
# Crea las filas del supermercado y las inicializa vacias
fila1 = []
fila2 = []

# Crear la lista de clientes que van entrando al supermercado
from random import randint
listaClientes = [ randint(0,5) for i in range(1,15) ]

# Ciclo for
for cliente in listaClientes:
    if len(fila2) < len(fila1):
        fila2.append(cliente)
    else:
        fila1.append(cliente)
    fila1.sort()
    fila2.sort()

print(f"fila 1: {fila1}")
print(f"fila 2: {fila2}")

#Opcion 2

# Crea las filas del supermercado y las inicializa vacias
fila1 = []
fila2 = []

# Ciclo while
cliente = input("Ingrese la prioridad del cliente: ")
while cliente != "":
    cliente = int(cliente)
    if len(fila2) < len(fila1):
        fila2.append(cliente)
    else:
        fila1.append(cliente)
    fila1.sort()
    fila2.sort()
    print(f"fila 1: {fila1}")
    print(f"fila 2: {fila2}")
    cliente = input("Ingrese la prioridad del cliente: ")