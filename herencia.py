class Persona:

    def __init__(self, nombre, rut, edad):
        self.nombre, self.rut = nombre, rut
        self.edad = edad
    
    def cumplirAños(self):
        self.edad += 1


class Alumno(Persona):

    def __init__(self, nombre, rut, edad, curso):
        super().__init__(nombre, rut, edad)
        self.curso = curso
    
    def cumplirAños(self):
        self.edad += 1
        self.curso = "1ro Universidad"


p = Persona("A", "1", 18)
print(f"Edad de {p.nombre} = {p.edad}")
p.cumplirAños()
print(f"Edad de {p.nombre} = {p.edad}")

a = Alumno("B", "2", 18, "4to Medio")
print(f"Edad de {a.nombre} = {a.edad} y esta en {a.curso}")
a.cumplirAños()
print(f"Edad de {a.nombre} = {a.edad} y esta en {a.curso}")

"""
__repr__ -> Determina como se ve print(objeto)
__add__ -> Determina el comportamiento de objA + objB
__mul__ -> Determina el comportamiento de objA * objB
__len__ -> Determina el comportamiento len(objeto)
"""