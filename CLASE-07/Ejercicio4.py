# Pida 2 datos int 
# sumelos 
# Muestre el resultado 

def RealizarOperacion():
    num1 = int(input("Digite un valor: "))
    num2 = int(input("Digite un valor: "))
    RealizarSuma(num1, num2)

def RealizarSuma(v1, v2):
    print(f"El resultado es: {v1+v2}")

RealizarOperacion()