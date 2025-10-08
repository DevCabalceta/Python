# Usted va a tener un metodo que es de retorno donde pida la edad de la persona
# Usted va a tener un metodo void que diga si la persona es mayor o menor de edad, 
# es decir, recibe un parametro
# Yo no quiero que usted en el metodo de pedir edad, llame al mostrar mayorEdad
# Pida el dato, guardelo en una variable y al metodo de tipo void enviele el insumo 
# o el dato de la edad


def PedirEdad():
    edad = int(input("Digite la edad: "))
    return edad


def MayorEdad(edadPersona):
    if edadPersona >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

edadPersona = PedirEdad()
MayorEdad(edadPersona)