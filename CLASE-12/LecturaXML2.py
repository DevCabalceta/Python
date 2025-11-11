import xml.etree.ElementTree as ET

class Curso:
    def __init__(self, codigoCurso, nombre, cantidadEstudiantes):
        self.codigoCurso = codigoCurso
        self.nombre = nombre
        self.cantidadEstudiantes = cantidadEstudiantes

vectorCursos = []
#cargue la informacion en el vector y digame cuantos estudiantes hay

# nombre del archivo
nombreArchivo = r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-12\EjemploInformacion.xml"

# parseo el XML
archivo = ET.parse(nombreArchivo)

root = archivo.getroot()

for curso in root.findall('curso'):
    codigo = curso.find('codigoCurso').text
    nombre = curso.find('nombre').text
    cantidad = int(curso.find('cantidadEstudiantes').text)
    nuevoCurso = Curso(codigo, nombre, cantidad)
    vectorCursos.append(nuevoCurso)

cantidadEstudiantesTotal = 0
for c in vectorCursos:
    cantidadEstudiantesTotal += c.cantidadEstudiantes

print(f"La cantidad total de estudiantes es de: {cantidadEstudiantesTotal}")