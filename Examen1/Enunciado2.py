# Pide al usuario un número entre 1 y 7 y muestra el día de la semana 
# correspondiente (1 = Lunes, 7 = Domingo). 

dia = int(input("Digite un numero entre 1 y 7: "))

match dia:
    case 1:
        print("El día seleccionado es Lunes")
    case 2:
        print("El día seleccionado es Martes")
    case 3:
        print("El día seleccionado es Miercoles")
    case 4:
        print("El día seleccionado es Jueves")
    case 5:
        print("El día seleccionado es Viernes")
    case 6:
        print("El día seleccionado es Sabado")
    case 7:
        print("El día seleccionado es Domingo")
    case __:
        print("Opción incorrecta, intente nuevamente.")