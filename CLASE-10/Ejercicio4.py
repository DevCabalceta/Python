
# Medias: Negras - Azules - Blancas
# medias = [N,A,A,A,B,B,N,N,A,B,N,N]
# Es que me diga cuantas medias de cada color hay
# 5 medias color negro
# 4 medias color azul
# 3 medias blancas

def contarCantidadColorMedias(vectorMedias, color):
    contador = 0

    for media in vectorMedias:
        if media == color:
            contador += 1

    return contador

medias = ["N","A","A","A","B","B","N","N","A","B","N","N"]

contadorNegras = contarCantidadColorMedias(medias, "N")
contadorBlancas = contarCantidadColorMedias(medias, "B")
contadorAzules = contarCantidadColorMedias(medias, "A")



print(f"Medias blancas: {contadorBlancas} \n"
      f"Medias negras: {contadorNegras} \n"
      f"Medias azules: {contadorAzules} \n")


#Cuantos pares de cada media puede formar
print(f"pares de medias blancas: {contadorBlancas//2}")
print(f"pares de medias negras: {contadorNegras//2}")
print(f"pares de medias azules: {contadorAzules//2}")

#Cuantos impares de cada media puede formar
print(f"Medias sueltas blancas: {contadorBlancas%2}")
print(f"Medias sueltas negras: {contadorNegras%2}")
print(f"Medias sueltas azules: {contadorAzules%2}")