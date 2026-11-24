dinero = 0

nombreProducto = str(input("Ingrese nombre de producto: "))
precioUnitarioProducto = int(input(f"Ingrese valor unitario de {nombreProducto}: "))
inventarioDisponible = int(input(f"Ingrese la cantidad de {nombreProducto} disponibles: "))

xVenta = int(input("Cuanto quiere vender?: "))

if inventarioDisponible >= xVenta:
    precioTotal = xVenta * precioUnitarioProducto
    dineroRecibido = int(input("Dinero recibido: "))
    if dineroRecibido >= precioTotal:
        print(f"Entraga vuelto: {dineroRecibido - precioTotal}")
        dinero += precioTotal
        inventarioDisponible -= xVenta
    else:
        precioTotal = 0
        xVenta = 0
        dinero += precioTotal
        inventarioDisponible -= xVenta

else:
    print("No se hizo la venta, porque no hay suficiente inventario.")