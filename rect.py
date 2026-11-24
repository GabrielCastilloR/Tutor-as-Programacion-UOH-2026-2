class rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def __repr__(self):
        salida = f"({self.base}, {self.altura})"
        return salida
    
    def calcularArea(self):
        area = self.base * self.altura
        return area
    
a = rectangulo(10, 15)
print(a.base, a.altura)
print(a.calcularArea()) #variable que guarda . metodo