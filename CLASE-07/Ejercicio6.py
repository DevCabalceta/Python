# Metodo de tipo retorno 
# Crear un metodo que pida un nombre y me devuelva el resultado 
# La voy a concatenar que el usuario digito en el metodo el nombre de: 

def PedirNombre():
    nombre = input("Digite el nombre a mostrar: ")
    return nombre

nombreDigitado = PedirNombre()
print(f"El usuario digito en el metodo el nombre de: {nombreDigitado}")