def PedirCiudades ():
    vectorCiudades = []
    for i in range(3):
        nombre = input("Inserte una ciudad")
        vectorCiudades.append(nombre)
    return vectorCiudades
#Metodo void que recibe parametros
def MostrarCiudades(vector):
    for c in vector: 
        print("Ciudad:", c )
#Metodo de tipo retorno que recibe parametro
def EliminarCiudades(vectorCiudades):
    vectorIndices = []
    for i in range(len(vectorCiudades)):
        if(len(vectorCiudades[i])>=7):
            vectorIndices.append(i)
    for indiceEliminar in vectorIndices:
        vectorCiudades.pop(indiceEliminar)
    
    return vectorCiudades


vectorCiudades = PedirCiudades()
MostrarCiudades(vectorCiudades)
vectorCiudades = EliminarCiudades(vectorCiudades)
print("-------------------")
MostrarCiudades(vectorCiudades)