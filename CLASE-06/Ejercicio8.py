# numeros = [5, -3, 8, 0, -1, 4]
# Sume solo los numeros positivos
# Cuantos numeros positivos hay

numeros = [5, -3, 8, 0, -1, 4]
TotalSuma = 0
positivos = 0

for n in numeros:
    if n > 0:
        TotalSuma += n
        positivos+=1

print(f"Resultado de la suma: {TotalSuma}")
print(f"Positivos: {positivos}")