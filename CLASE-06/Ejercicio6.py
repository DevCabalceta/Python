

vectorPrueba = ["Gabriel"]

vectorPrueba.append("Ricardo")
vectorPrueba.append("Adolfo")
vectorPrueba.append("Natalia")
vectorPrueba.append("Samuel")

# Volarse un texto vector 
vectorPrueba.remove("Adolfo")

# Volarse una posicion
vectorPrueba.pop(3)

# Quiero limpiar el vector
vectorPrueba.clear()

for o in vectorPrueba:
    print("El nombre es: ", o) 