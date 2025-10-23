import pandas as pd

class Persona:
    def __init__(self,nombre, apellido, mate, ciencias, sociales):
        self.nombre = nombre
        self.apellido = apellido
        self.mate = mate
        self.ciencias = ciencias
        self.sociales = sociales

hoja = pd.read_excel(r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-11\EjemploInformacion.xlsx",  
                      sheet_name="Hoja3",
                      engine="openpyxl")


vectorPersonas = []

for _, row in hoja.iterrows():
    mate = 0
    ciencias = 0
    sociales = 0

    if pd.notna(row["Mate"]):
        mate = row["Mate"]
    
    if pd.notna(row["Ciencias"]):
        ciencias = row["Ciencias"]

    if pd.notna(row["Sociales"]):
        sociales = row["Sociales"]

    persona = Persona(row["Nombre"], row["Apellido"], mate, ciencias, sociales)
    vectorPersonas.append(persona)

promedioMate = 0
promedioCiencias = 0
promedioSociales = 0

for estudiante in vectorPersonas:
    promedioMate      += float(estudiante.mate)
    promedioCiencias  += float(estudiante.ciencias)
    promedioSociales  += float(estudiante.sociales)

PromedioGeneralMate = promedioMate / len(vectorPersonas)
PromedioGeneralCiencias = promedioCiencias / len(vectorPersonas)
PromedioGeneralSociales =  promedioSociales / len(vectorPersonas)

df_resultadosPromedio = pd.DataFrame({
    "Asignatura": ["Matematica", "Ciencias", "Sociales"],
    "Promedio": [PromedioGeneralMate, PromedioGeneralCiencias, PromedioGeneralSociales]
})

with pd.ExcelWriter(
        r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-11\EjemploInformacion.xlsx", 
        engine="openpyxl", 
        mode="a",
        if_sheet_exists="new"
    ) as writer:
    df_resultadosPromedio.to_excel(
        writer, 
        sheet_name="Resultados",
        index= False
    )