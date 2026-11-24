class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__variable = "secreto"
    
    def revelarSecreto(self):
        print(self.__variable)

    def __repr__(self): # str(objeto)
        return f"({self.x}, {self.y})"

    def __add__(self, otroVector):
        sumaX = self.x + otroVector.x
        sumaY = self.y + otroVector.y
        return Vector(sumaX, sumaY)

    def __mul__(self, otroVector):
        if type(otroVector) == Vector:
            #(a, b)*(c,d) = a*c + b*d
            return self.x*otroVector.x + self.y*otroVector.y
        elif type(otroVector) == float or type(otroVector) == int:
            #a*(b, c) = (a*b, a*c)
            return Vector(self.x*otroVector, self.y*otroVector)
        else:
            return None
    
    def __rmul__(self, otroVector):
        return self.__mul__(otroVector)

x = 10
y = 15
print(x + y)
vecA = Vector(x,y)
#vecB = Vector(2*x, y+1)
#print(vecA + vecB)
#print(vecA * vecB)
#print(vecA, 3*vecA)