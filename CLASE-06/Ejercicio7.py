# Vector vacio 
# Usted va a ingresar 5 numeros aleatorios 
# Despues muestre 

# Primero, logre pedir 5 numeros
# Segundo, trate de ingresarlos al vector append 
# Tercero, muestre que hay en ese vector

numerosAleatorios = []

# Opcion1
# for i in range(5):
#     numero = int(input("Digite numero: "))
#     numerosAleatorios.append(numero)

# Opcion2
contador = 1
while contador <= 5:
    numero = int(input("Digite numero: "))
    numerosAleatorios.append(numero) 
    contador += 1

for n in numerosAleatorios:
    print(f"Los numeros ingresados son: {n}")
