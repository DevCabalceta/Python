import xml.etree.ElementTree as ET
from xml.dom import minidom

# =====================
#   CLASES DEL MODELO
# =====================
class Curso:
    def __init__(self, idCurso, nombre):
        self.idCurso = idCurso
        self.nombre = nombre


class Estudiante:
    def __init__(self, idEstudiante, nombre, edad, correo, cursos):
        self.idEstudiante = idEstudiante
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.cursos = cursos  


# ============================
#   CREACIÓN DE LOS 6 CURSOS
# ============================
cursos = [
    Curso(1, "Python Fundamentos"),
    Curso(2, "Front End Developer"),
    Curso(3, "Ciberseguridad"),
    Curso(4, "SQL Server"),
    Curso(5, "Linux"),
    Curso(6, "Amazon Web Services")
]

# ===============================
#   CREACIÓN DE LOS 10 ESTUDIANTES
# ===============================
estudiantes = [
    Estudiante(1, "Carlos Molina", 20, "carlos@vla.com", [cursos[0], cursos[1]]),
    Estudiante(2, "Ana García", 22, "ana@vla.com", [cursos[2]]),
    Estudiante(3, "Luis Fernández", 19, "luis@vla.com", [cursos[0], cursos[2], cursos[3]]),
    Estudiante(4, "María López", 18, "maria@vla.com", [cursos[1], cursos[3], cursos[4], cursos[5]]),
    Estudiante(5, "David Sánchez", 21, "david@vla.com", [cursos[4]]),
    Estudiante(6, "Gabriel Cortés", 23, "gabriel@vla.com", [cursos[5], cursos[0], cursos[1]]),
    Estudiante(7, "Daniela Vargas", 20, "daniela@vla.com", [cursos[3], cursos[4], cursos[5]]),
    Estudiante(8, "Roberto Castro", 24, "roberto@vla.com", [cursos[2], cursos[3]]),
    Estudiante(9, "Paula Jiménez", 19, "paula@vla.com", [cursos[1]]),
    Estudiante(10, "Sofía Méndez", 22, "sofia@vla.com", [cursos[0], cursos[1], cursos[2], cursos[3], cursos[4]])
]

# =======================================
#   GENERAR EL ARCHIVO XML
# =======================================
root = ET.Element("estudiantes")

for est in estudiantes:
    nodo_est = ET.SubElement(root, "estudiante")

    ET.SubElement(nodo_est, "idEstudiante").text = str(est.idEstudiante)
    ET.SubElement(nodo_est, "nombre").text = est.nombre
    ET.SubElement(nodo_est, "edad").text = str(est.edad)
    ET.SubElement(nodo_est, "correo").text = est.correo

    nodo_cursos = ET.SubElement(nodo_est, "cursos")

    for curso in est.cursos:
        nodo_curso = ET.SubElement(nodo_cursos, "curso")
        ET.SubElement(nodo_curso, "idCurso").text = str(curso.idCurso)
        ET.SubElement(nodo_curso, "nombre").text = curso.nombre

#======================Ruta del archivo===================================================
ruta_archivo = r"C:\Users\Gabriel Cabalceta\Documents\Python\Examen2\EstudiantesVLA.xml"

#======================Para formatear el archivo==========================================
xml_str = ET.tostring(root, encoding='utf-8')
xml_pretty = minidom.parseString(xml_str).toprettyxml(indent="   ")

with open(ruta_archivo, "w", encoding="utf-8") as f:
    f.write(xml_pretty)

print("Archivo XML creado con éxito en:")
print(ruta_archivo)
