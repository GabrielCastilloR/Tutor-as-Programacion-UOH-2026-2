"""
Enunciado:
    Calcular de forma recursiva la sumatoria de 1/k^2, asumiendo que k es un natural
"""

def sumatoria(n):
    # Caso Base
    if (n == 1):
        return 1
    
    # Paso recursivo
    else:
        suma = 1/(n**2) + sumatoria(n-1) # 1/n^2 + 1/(n-1)^2 + .... 1/1^2
        return suma

"""
Enunciado:
    Calcular el k-esimo termino de la sucesión a_i = a_(i-1) * a_(i-2), con a_0 = 1 y a_1 = 1.2
"""

def sucesion(k):

    if (k == 0):
        return 1
    elif(k == 1):
        return 1.2
    else:
        return sucesion(k-1) * sucesion(k-2) # Paso recursivo

"""
Enunciado:
    Retornar una lista con los k primeros de la sucesión a_i = a_(i-1) * a_(i-2), con a_0 = 1 y a_1 = 1.2
"""
def sucesionLista(k):
    # Caso base
    if (k == 1) or (k == 0):
        return [1, 1.2]
    
    # Caso recursivo
    else:
        listaAnteriores = list(sucesionLista(k-1))
        a_k = listaAnteriores[-1] * listaAnteriores[-2]
        listaAnteriores.append(a_k)
        return listaAnteriores

print(sucesionLista(3))