import xml.etree.ElementTree as ET

class Persona:
    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)

# nombre del archivo
nombreArchivo = r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-11\Prueba.xml"

# parseo el XML
arbol = ET.parse(nombreArchivo)
principal = arbol.getroot()

vectorPersonas = []

for persona_xml in principal.findall("persona"):
    nombre = persona_xml.find("nombre").text
    apellido = persona_xml.find("apellido").text
    edad = persona_xml.find("edad").text

    persona = Persona(nombre, apellido, edad)
    vectorPersonas.append(persona)

for p in vectorPersonas:
    print(p.nombre, p.apellido, p.edad)
