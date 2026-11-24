"""
funcion(instancia 1) -> instancia 2 -> instancia 3 = x
x -> instancia 2 = x + y -> instancia 1 = x + y + z
"""

"""
Enunciado: subdividir un string cada vez que aparezce el caracter , en el string original
sin usar str.split()
"""

def split(string):
    
    # Caso base
    if string == "": # Si el string es vacio
        return [""]
    if not "," in string: # Si no está el separador en el string
        return [string]
    
    # Caso recursivo
    else:
        for i in range(0, len(string)): # Itera sobre el string
            if string[i] == ",": # Cuando encuentra el separador, hace el llamado recursivo
                return [string[0:i]] + split(string[i+1:]) # Concatena las listas para entregar solo una. #El error que se produjo en tutoria paso porque el llamado recursivo usaba split(string[i:]), en vez de split(string[i+1:]), pero como i es la posicion del separador, todas las llamadas recursivas tenian un separador y se creo un loop infinito

print(split("Hola, Mundo!"))


"""
Enunciado:
    Calcular la posicion n = 100 de la sumatoria a_n = n^2
"""

def sumatoria(n):
    if (n == 1):
        return 1
    else:
        suma = sumatoria(n-1) + n**2
        return suma

# n(n+1)(2n+1)/6 -> 100*101*201/6 = 338.350
#print(sumatoria(100))

"""
factorial
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(5))