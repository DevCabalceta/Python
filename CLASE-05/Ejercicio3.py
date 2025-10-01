

vectorNotas = [89, 98, 76, 89, 90]

print(f"valor: {vectorNotas[4]}")

for i in range(len(vectorNotas)):
    if vectorNotas[i] >= 90:
        print("Excelente")
    else:
        print("Deberia ponerle mas al curso")
