numero1 = int(input("Digite primer numero: "))
numero2 = int(input("Digite segundo numero: "))
resultado = 0

if numero1 < 0 or numero2 <0 :
    print("La suma no se puede realizar")
else:
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
