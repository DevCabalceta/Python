class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

def ValidarExistePersona(listaPersonas):
    nombre = input("Digite un nombre: ")
    bandera = False #No existe la persona

    for per in listaPersonas:
        if(per.nombre.upper() == nombre.upper()):
            bandera = True
            break

    if bandera == True:
        print("Existe el nombre")
    else:
        print("No exite el nombre")
        
listaPersonas = []
persona1 = Persona("Adolfo")
persona2 = Persona("Juan")
persona3 = Persona("Diego")
persona4 = Persona("Natalia")
persona5 = Persona("Samuel")

listaPersonas.append(persona1)
listaPersonas.append(persona2)
listaPersonas.append(persona3)
listaPersonas.append(persona4)
listaPersonas.append(persona5)
ValidarExistePersona(listaPersonas)



