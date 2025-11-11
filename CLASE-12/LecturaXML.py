import xml.etree.ElementTree as ET

# nombre del archivo
nombreArchivo = r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-12\EjemploInformacion.xml"

# parseo el XML
archivo = ET.parse(nombreArchivo)

root = archivo.getroot()

for curso in root.findall('curso'):
    codigo = curso.find('codigoCurso').text
    nombre = curso.find('nombre').text
    cantidad = curso.find('cantidadEstudiantes').text

    print(f"Codigo: {codigo}, Nombre: {nombre}, Cantidad: {cantidad}")