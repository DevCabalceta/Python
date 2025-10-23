import pandas as pd

hoja1 = pd.read_excel(r"C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-11\EjemploInformacion.xlsx", sheet_name="Hoja1", engine="openpyxl", header=None)

vector_numeros = hoja1.iloc[:,0].tolist()

for numero in vector_numeros:
    print(numero)