
# Medias: Negras - Azules - Blancas
# medias = [N,A,A,A,B,B,N,N,A,B,N,N]
# Es que me diga cuantas medias de cada color hay
# 5 medias color negro
# 4 medias color azul
# 3 medias blancas

medias = ["N","A","A","A","B","B","N","N","A","B","N","N"]
mblancas = 0
mnegras = 0
mazules = 0

for m in medias:
    if m == "N":
        mnegras = mnegras + 1
    elif m == "A":
        mazules = mazules + 1
    else:
        mblancas = mblancas + 1

print(f"Medias blancas: {mblancas} \n"
      f"Medias negras: {mnegras} \n"
      f"Medias azules: {mazules} \n")


#Cuantos pares de cada media puede formar

print(f"pares de medias blancas: {mblancas//2}")
print(f"pares de medias negras: {mnegras//2}")
print(f"pares de medias azules: {mazules//2}")