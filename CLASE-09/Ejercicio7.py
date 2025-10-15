# Convertir las vocales a mayuscula

palabraAConvertir = "octubre"
nuevaPalabra = ""

for posicion in range(len(palabraAConvertir)):
    letra = palabraAConvertir[posicion]

    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        nuevaPalabra = nuevaPalabra + letra.upper()
    else:
        nuevaPalabra = nuevaPalabra + letra.lower()

print(f"La palabra convertir es: {nuevaPalabra}")