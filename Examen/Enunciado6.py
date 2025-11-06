# Crea una clase Rectángulo con atributos ancho y alto. Agrega un método área() que 
# calcule el área. Crea un objeto y muestra su área.

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


ancho = float(input("Digite el ancho del rectángulo: "))
alto = float(input("Digite el alto del rectángulo: "))

operacion = Rectangulo(ancho, alto)
print(f"El área del rectángulo es: {operacion.area()}")
