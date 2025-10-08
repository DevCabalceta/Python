# Quiero saber los datos personales de una persona 
# nombre, edad, correo 
# concatene toda la informacion 



def PedirNombre():
    nombre = input("Digite el nombre: ")
    return nombre

def PedirEdad():
    edad = input("Digite la edad: ")
    return edad

def PedirCorreo():
    correo = input("Digite el correo: ")
    return correo

nombreDigitado = PedirNombre()
edadDigitado = PedirEdad()
correoDigitado = PedirCorreo()

print(f"La informacion del usario es la siguiente: \n"
      f"Nombre: {nombreDigitado}\n"
      f"Edad: {edadDigitado}\n"
      f"Correo: {correoDigitado}\n")

