import xml.etree.ElementTree as ET

#======================Ruta del archivo Ejercicio1===================================
ruta_archivo = r"C:\Users\Gabriel Cabalceta\Documents\Python\Examen2\EstudiantesVLA.xml"

#======================Cargar el XML=================================================
tree = ET.parse(ruta_archivo)
root = tree.getroot()

# ----------------------------
# 1) Cantidad de cursos por estudiante
# ----------------------------
print("Cantidad de cursos por estudiante:\n")

for estudiante in root.findall("estudiante"):
    nombre = estudiante.find("nombre").text
    cursos = estudiante.find("cursos").findall("curso")
    cantidad = len(cursos)

    print(f"- {nombre} lleva {cantidad} cursos.")

# ----------------------------
# 2) Los cursos que lleva cada estudiante
# ----------------------------
print("\nCursos que lleva cada estudiante:\n")

for estudiante in root.findall("estudiante"):
    nombre = estudiante.find("nombre").text
    cursos = estudiante.find("cursos").findall("curso")

    lista_cursos = [c.find("nombre").text for c in cursos]

    print(f"- {nombre}: {', '.join(lista_cursos)}")

# ----------------------------
# 3) Lista de cursos SIN REPETIR
# ----------------------------
print("\nLista de cursos disponibles:\n")

setCursos = set()  # Para eliminar duplicados

for estudiante in root.findall("estudiante"):
    cursos = estudiante.find("cursos").findall("curso")
    for c in cursos:
        setCursos.add(c.find("nombre").text)

for curso in setCursos:
    print(f"- {curso}")

