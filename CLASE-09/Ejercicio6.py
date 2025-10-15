palabra = "Clase"
for letra in palabra:
    print(letra)
for posicion in range(len(palabra)):
    print(palabra[posicion])
letra = "h"
print(letra.upper())
numero = 4
if numero%2 == 0:
    print("El numero es par")

# Obtenga una palabra
# A las letras pares, conviertalas en mayuscula
# A las letras impares, conviertalas a minuscula
# Y muestreme la palabra final

palabraAConvertir = "octubre"
nuevaPalabra = ""

for posicion in range(len(palabraAConvertir)):
    letra = palabraAConvertir[posicion]

    if posicion%2 == 0:
        nuevaPalabra = nuevaPalabra + letra.upper()
    else:
        nuevaPalabra = nuevaPalabra + letra.lower()

print(f"La palabra convertir es: {nuevaPalabra}")

