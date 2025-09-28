
while True:

    operacion = int(input("1. Sumar\n" 
                          "2. Restar\n" 
                          "3. Multiplicar\n" 
                          "4. Dividir\n"
                          "5. Salir\n\n"
                          "Digite una opcion: "))
    
    match operacion:
        case 1:
            n1 = int(input("Digite primer numero: "))
            n2 = int(input("Digite segundo numero: "))
            resultado = n1 + n2
            print(f"El resultado de la operacion es: {resultado}")
        case 2:
            n1 = int(input("Digite primer numero: "))
            n2 = int(input("Digite segundo numero: "))
            resultado = n1 - n2
            print(f"El resultado de la operacion es: {resultado}")
        case 3:
            n1 = int(input("Digite primer numero: "))
            n2 = int(input("Digite segundo numero: "))
            resultado = n1 * n2
            print(f"El resultado de la operacion es: {resultado}")
        case 4:
            n1 = int(input("Digite primer numero: "))
            n2 = int(input("Digite segundo numero: "))
            if n1 == 0 or n2 == 0:
                print("El resultado de la operacion es: 0")
            else:
                resultado = n1 / n2
                print(f"El resultado de la operacion es: {resultado}")
        case 5:
            print("Saliendo de la calculadora")
            break
        case _:
            print("Opcion incorrecta, digite nuevamente")



