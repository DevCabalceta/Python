

# Digame los numeros pares y los impares
vectorNumeros = [7,44,23,8,2,99]

textoPares = ""
textoImpares = ""

for numero in vectorNumeros:
    if(numero%2 == 0):
        textoPares = textoPares + "," + str(numero)
    else:
        textoImpares = textoImpares + "," + str(numero)


print(f"Los numeros pares son: {textoPares}")
print(f"Los numeros pares son: {textoImpares}")


# Digame cuantos pares e impares hay
pares = 0
impares = 0
for numero in vectorNumeros:
    if(numero%2 == 0):
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")

# Opcion 3 

vectorPares = []
vectorImpares = []

for numero in vectorNumeros:
    if(numero%2 == 0):
        vectorPares.append(numero)
    else:
        vectorImpares.append(numero)

print(f"Los numeros pares son: {len(vectorPares)}")
print(f"Los numeros pares son: {len(vectorImpares)}")