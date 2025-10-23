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

    if pd.notna(row["Mate"]) and pd.notna(row["Ciencias"]) and pd.notna(row["Sociales"]):
        persona = Persona(row["Nombre"], row["Apellido"],row["Mate"], row["Ciencias"], row["Sociales"])
        vectorPersonas.append(persona)
    else:
        print("Estudiante con informacion incompleta: ", row["Nombre"])

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


# vectorPersonas = []

# for _, row in hoja3.iterrows():
#     mate = 0
#     ciencias = 0
#     sociales = 0

#     if pd.notna(row["Mate"]):
#         mate = row["Mate"]
    
#     if pd.notna(row["Ciencias"]):
#         ciencias = row["Ciencias"]

#     if pd.notna(row["Sociales"]):
#         sociales = row["Sociales"]

#     persona = Persona(row["Nombre"], row["Apellido"], mate, ciencias, sociales)
#     vectorPersonas.append(persona)

# promedioMate = 0
# promedioCiencias = 0
# promedioSociales = 0

# for estudiante in vectorPersonas:
#     promedioMate      += float(estudiante.mate)
#     promedioCiencias  += float(estudiante.ciencias)
#     promedioSociales  += float(estudiante.sociales)

# print("Promedio Matemática:", promedioMate / len(vectorPersonas))
# print("Promedio Ciencias:",    promedioCiencias / len(vectorPersonas))
# print("Promedio Sociales:",    promedioSociales / len(vectorPersonas))