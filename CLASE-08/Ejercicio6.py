class Animal:
    def __init__(self, pnombre, pcolor, pedad):
        self.nombre = pnombre
        self.color = pcolor
        self.edad = pedad

    def VerAnimal(self):
        print(f"Datos: {self.nombre}, {self.color}, {self.edad}")

listaAnimales = []

for i in range(3):
    nombre = input("Digite un nombre: ")
    color = input("Digite un color: ")
    edad = input("Digite la edad del animal: ")
    animal = Animal(nombre, color, edad)
    listaAnimales.append(animal)

for animalito in listaAnimales:
    animalito.VerAnimal()


