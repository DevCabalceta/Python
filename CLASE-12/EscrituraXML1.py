import xml.etree.ElementTree as ET

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

vectorPersonas = []
persona1 = Persona('Adolfo', 33)
persona2 = Persona('Angie', 30)
persona3 = Persona('Sophia', 1)

vectorPersonas.append(persona1)
vectorPersonas.append(persona2)
vectorPersonas.append(persona3)

root = ET.Element('listaPersonas')

for persona in vectorPersonas:
    #Crear una persona en el root (listaPersonas)
    personaElement = ET.SubElement(root, 'persona')

    #Crear cada uno de los atributos
    nombreElemento = ET.SubElement(personaElement, 'nombre')
    nombreElemento.text = persona.nombre

    #Crear cada uno de los atributos
    edadElemento = ET.SubElement(personaElement, 'edad')
    edadElemento.text = str(persona.edad)

arbol = ET.ElementTree(root)

arbol.write("Personas1.xml", encoding="utf-8", xml_declaration=True)