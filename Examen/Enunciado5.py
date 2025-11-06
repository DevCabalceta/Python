# Crea una lista con los números del 1 al 50. Recorre la lista con un for y muestra solo 
# los números pares. 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

pares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)

for p in pares:
    print(f"Par: {p}")
