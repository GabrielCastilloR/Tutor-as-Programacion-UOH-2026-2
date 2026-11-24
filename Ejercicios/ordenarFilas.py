# Crea las filas del supermercado y las inicializa vacias
filas = [[],[],[],[],[]]

# Ciclo while
cliente = input("Ingrese la prioridad del cliente: ")
while cliente != "-1":
    cliente = int(cliente)
    masCorta = 0
    for i in range(1, len(filas)):
        if len(fila) < len(fila[masCorta]):
            masCorta = i
    
    fila[masCorta].append(cliente)
    fila[masCorta].sort()
    
for i in range(0, len(filas)):
    print(f"Fila #{i}: {filas[i]}")