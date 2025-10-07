# Cajon con las medias 
# Medias Blancas = B 
# Medias Negras = N 
# [B,B,B,N,B,N,B,N,N,N,N]
# Cuantas medias blancas y negras hay? 

medias = ["B","B","B","N","B","N","B","N","N","N","N"]

blancas = 0
negras = 0


for media in medias:
    if media == "B":
        blancas += 1
    else:
        negras += 1

print(f"Medias blancas: {blancas} \n"
      f"Medias negras: {negras}")