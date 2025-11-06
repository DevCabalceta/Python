# • Crea un juego donde el programa intenta adivinar el número que el usuario piensa 
# (entre 1 y 100): 
# • Usa un algoritmo de búsqueda binaria para adivinar el número en el menor 
# número de intentos posible. 
# • El usuario responde con "mayor", "menor" o "correcto".

print("¡Piensa en un número entre 1 y 100!")

minimo = 1
maximo = 100
intentos = 0
respuesta = ""

while respuesta != "correcto":
    intento = (minimo + maximo) // 2
    intentos += 1
    print(f"\n¿Tu número es {intento}?")
    respuesta = input("Responde con 'mayor', 'menor' o 'correcto': ").lower()

    if respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1
    elif respuesta == "correcto":
        print(f"\n¡Adiviné tu número en {intentos} intentos!")
    else:
        print("Por favor, responde solo con 'mayor', 'menor' o 'correcto'.")

print("Gracias por jugar")
