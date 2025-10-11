class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

persona1 = Persona("Gabriel", 24, "gabriel@gmail.com")
persona2 = Persona("Ari", 22, "ari@gmail.com")
persona2 = Persona("Dilson", 25, "dilson@gmail.com")

print(f"El nombre es: {persona2.nombre}, correo: {persona2.correo}")