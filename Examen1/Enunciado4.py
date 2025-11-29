# Escribe un programa que pida números al usuario hasta que ingrese el número 0. 
# Luego muestra la suma de todos los números ingresados (excepto el 0).

suma = 0  

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break 
    suma += numero  

print(f"La suma de los números ingresados es: {suma}")