class Alumno:

    # Funcion constructora
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre
    
    # Metodo
    def cambioCarrera(self, nuevaCarrera):
        self.carrera = nuevaCarrera


# Crear un objeto / Inicializar un objeto
alumno1 = Alumno("Yulianny", "Ing. Civil, plan comun")

print(alumno1) # Ejemplo incorrecto
print(alumno1.nombre, alumno1.carrera) # Ejemplo correcto

alumno1.cambioCarrera("Ing. Civil Electrica")
print(alumno1.nombre, alumno1.carrera)

# Propiedad: Es cualquier adjetivo aplicable al objeto
# Descriptor Identificante: Es una propiedad que además sirve para diferenciar a una instancia del objeto de todas las demás instancias
# Método: Es un proceso que el objeto es capaz de realizar

