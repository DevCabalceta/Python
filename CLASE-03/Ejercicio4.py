
operacion = int(input("1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n Elija una operacion: "))
numero1 = float(input("Digite primer numero: "))
numero2 = float(input("Digite segundo numero: "))
resultado = 0

if operacion == 1:
    resultado = numero1 + numero2
elif operacion == 2:
    resultado = numero1 - numero2
elif operacion == 3:
    resultado = numero1 * numero2
elif operacion == 4:
    if numero2 == 0:
        resultado = 0
    else:
        resultado = numero1 / numero2
else:
    resultado = 0

print("El resultado de la operacion es: ", resultado)