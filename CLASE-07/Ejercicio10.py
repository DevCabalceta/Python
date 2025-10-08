def PedirCiudades ():
    vectorCiudades = []
    for i in range(3):
        nombre = input("Inserte una ciudad: ")
        vectorCiudades.append(nombre)
    return vectorCiudades
#Metodo void que recibe parametros
def MostrarCiudades(vector):
    for c in vector: 
        print("Ciudad:", c )
#Metodo de tipo retorno que recibe parametro
def EliminarCiudades(vectorCiudades):
    ciudadesFiltradas = []
    for ciudad in vectorCiudades:
        if len(ciudad)<=7:
            ciudadesFiltradas.append(ciudad)
    
    return ciudadesFiltradas
vectorCiudades = PedirCiudades()
MostrarCiudades(vectorCiudades)
vectorCiudades = EliminarCiudades(vectorCiudades)
print("-------------------")
MostrarCiudades(vectorCiudades)