precios = {"lapiz":150, "cuaderno":1200, "goma":300}

print(f"Cuaderno: {precios["cuaderno"]}")

precios["regla"] = 500

llaves = precios.keys()
for llave in llaves:
    print(f"{llave}: ${precios[llave]}")