
listaPersonas = []

# Opcion 1
contador  = 1
while contador <= 3:
    nombre = input("Digite nombre: ")
    listaPersonas.append(nombre)
    contador = contador + 1

# Opcion 2
for i in range (3):
    nombre = input("Digite nombre: ")
    listaPersonas.append(nombre)

for p in listaPersonas:
    print(f"Persona: {p}")