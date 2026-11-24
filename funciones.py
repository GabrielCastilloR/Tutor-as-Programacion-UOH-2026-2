"""
def miFuncion(args):
    #instrucciones
    return miVariable


miFuncion(args) # Si no tiene retorno
variable = miFuncion(args) #Si tiene retorno
"""

def sumar(a, b):
    c = a + b
    return c

listaA = [i for i in range(0, 20)]
listaB = [2*i for i in range(0,20)]

def compararLargos(lista1, lista2):
    largo1 = len(lista1)
    largo2 = len(lista2)
    if largo1 > largo2:
        return f"La lista {lista1} es la mas larga."
    elif largo2 > largo1:
        return f"La lista {lista2} es la mas larga."
    else:
        return "Las listas son iguales en largo."


def fibonacci(n):
    #Definicion de los casos base
    if (n == 0) or (n == 1):
        return n
    
    #Paso recursivo
    else:
        # A_n = A_n-1 + A_n-2
        valor = fibonacci(n-1) + fibonacci(n-2)
        return valor

# 0 1 1 2 3 5 8 13 21 34
# print(fibonacci(10))

def openFile(fname):
    with open(fname, "r+") as f:
        lineas = f.readlines()
        for i in range(0, len(lineas)):
            lineas[i] = lineas[i].strip("\n").split(",")
        f.close()
        return lineas

print(openFile("datos.csv"))
