

Semeforo = "rojo"


#Opcion IF
if Semeforo == "verde":
    print("Maneje sin problemas")
elif Semeforo == "Amarillo":
    print("Vaya frenando")
else:
    print("Detengase")


#Opcion MATCH
match Semeforo:
    case "verde":
        print("Maneje sin problemas")
    case "Amarillo":
        print("Vaya frenando")
    case "rojo":
        print("Detengase")
    case __:
        print("El valor no es valido")