import json 

#Abrir el archivo
with open(r'C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-12\EjemploInformacion.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

for curso in data["cursos"]:
    print(f"Codigo: {curso['codigoCurso']}")
    print(f"Nombre: {curso['nombre']}")
    print(f"Cantidad: {curso['cantidadEstudiantes']}")