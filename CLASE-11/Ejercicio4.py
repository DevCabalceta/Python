import pandas as pd

class Persona:
    def __init__(self,nombre, apellido, mate, ciencias, sociales):
        self.nombre = nombre
        self.apellido = apellido
        self.mate = mate
        self.ciencias = ciencias
        self.sociales = sociales

hoja3 = pd.read_excel(r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-11\EjemploInformacion.xlsx", 
                      sheet_name="Hoja4",
                      engine="openpyxl")


vectorPersonas = []

for _, row in hoja3.iterrows():
    persona = Persona(row["Nombre"], row["Apellido"],row["Mate"], row["Ciencias"], row["Sociales"])
    vectorPersonas.append(persona)

promedioMate = 0
promedioCiencias = 0
promedioSociales = 0

for estudiante in vectorPersonas:
    promedioMate      += float(estudiante.mate)
    promedioCiencias  += float(estudiante.ciencias)
    promedioSociales  += float(estudiante.sociales)

print("Promedio Matemática:", promedioMate / len(vectorPersonas))
print("Promedio Ciencias:",    promedioCiencias / len(vectorPersonas))
print("Promedio Sociales:",    promedioSociales / len(vectorPersonas))