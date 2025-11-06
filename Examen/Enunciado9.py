# • Escribe un programa que: 
# o Pida al usuario 5 números enteros y los guarde en una lista. 
# o Muestre:  
# ▪ La lista original. 
# ▪ El número mayor y el número menor. 
# ▪ La suma y el promedio de los números.

lista = []

for i in range(5):
    numero = int(input("Digite número entero: "))
    lista.append(numero)

print("\nLista original:", lista)


mayor = max(lista)
menor = min(lista)
suma = sum(lista)
promedio = suma / len(lista)

print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")