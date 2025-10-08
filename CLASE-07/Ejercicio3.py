# Quiero tener un metodo reciba por parametro un vector 
# Metodo muestre lo que hay en el vector 
# Ese vector es de nombre 

nombre = ["Dilson","Abel","Dayana","Adolfo"]
nombre_2 = ["Alberto","Johel","Gabriel","Adolfo"]

def MostrarDatosVector(vectorNombres):
    for persona in vectorNombres:
        print(f"Persona: {persona}")

MostrarDatosVector(nombre)
MostrarDatosVector(nombre_2)