# Va a contar hasta el numero 10 
# Y con un metodo digame si el numero es par o es impar 

# opcion1
# numeros = [1,2,3,4,5,6,7,8,9,10]

# def EsPar(numero):
#     for n in numero:
#         if n % 2 == 0:
#             print("Par")
#         else:
#             print("Impar")


# EsPar(numeros)

# opcion2
def EsPar(numero):
    if numero % 2 == 0:
        print(f"El numero: {numero} es Par")
    else:
        print(f"El numero: {numero} es Impar")


contador = 1
while contador <= 10:
    EsPar(contador)
    contador+=1