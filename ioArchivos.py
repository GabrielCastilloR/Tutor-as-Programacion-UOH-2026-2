with open("datos.csv", "r+") as f:
    lineas = f.readlines()
    f.close()

for i in range(0, len(lineas)):
    lineas[i] = lineas[i].replace("\n", "")
    lineas[i] = lineas[i].split(",")
    if i > 0:
        lineas[i][1] = int(lineas[i][1])
        lineas[i][2] = int(lineas[i][2])
    lineas[i] = tuple(lineas[i])

total = 0
for producto in lineas[1:]:
    print(producto[0] + f" {producto[1] * producto[2]}")
    total += producto[1] * producto[2]

for producto in lineas[1:]:
    if (producto[1] < 10) or (producto[2] > 1000):
        print(producto[0])

print(f"El total es: {total}")