# Cual es el numero mayor

numeros = [12,5,34,7,22,17]
mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print(f"Numero mayor: {mayor}")
    