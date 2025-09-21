# Usted va a pedir un valor string que pida un color
# Si es el color == verde entonces digales a la persona que felicidades, pego el color, si no 
# Siga intentado

while True:
    color = input("Digite un color: ").lower()
    if color == "verde":
        print("Felicidades, pego el color verde")
        break  # Sale del bucle cuando la entrada es válida
    else:
        print("Color invalido, siga intentado.")