import pandas as pd

class Persona:
    def __init__(self, nombre, apellido, edad, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula

def VerificarExistenciaIdentificacion(numeroId, vectorPersonas):
    existeUsuario = False

    for p in vectorPersonas:
        if p.cedula == numeroId:
            existeUsuario = True
            break

    return existeUsuario

hoja2 = pd.read_excel(r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-11\EjemploInformacion.xlsx", sheet_name="Hoja2", engine="openpyxl")

vectorPersonas = [Persona(row["Nombre"],row["Apellido"],row["Edad"],row["Identificacion"]) for _, row in hoja2.iterrows()]

for p in vectorPersonas:
    print(p.nombre)

existeIdExcel = VerificarExistenciaIdentificacion(30467045, vectorPersonas)

if existeIdExcel == True:
    print("Si existe la identificacion en el excel")
else:
    print("No existe la cedula en el excel")
