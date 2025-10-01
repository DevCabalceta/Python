
nombres = ["Adolgo", "Stevy", "Adolfo", "Gabriel", "Gabriel", "Dilson", "Ari", "Adilfo", "Mayte", "Adolfo"]

contador = 0

for i in range(len(nombres)):
    if nombres[i] == "Gabriel":
        contador += 1

print(f"Gabriel esta {contador} veces")
