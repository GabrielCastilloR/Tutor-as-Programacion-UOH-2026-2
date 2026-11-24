filas = [[],[],[],[],[]] # Define una variable con 5 filas para las cajas de la tienda

prioridadCliente = int(input("Ingrese el número del cliente:"))

while prioridadCliente > -1:
    indiceMasCorta = 0 # Indice de la fila más corta
    for i in range(1, len(filas)):
        if len(filas[i]) < len(filas[indiceMasCorta]):
            indiceMasCorta = i
    filas[indiceMasCorta].append(prioridadCliente)
    filas[indiceMasCorta].sort()
    prioridadCliente = int(input("Ingrese el número del cliente:"))

for i in range(0, len(filas)):
    print(f"Fila #{i+1}: {filas[i]}")