dias = input("Lunes\n" 
             "Martes\n" 
             "Miercoles\n" 
             "Jueves\n"
             "Viernes\n" 
             "Sabado\n" 
             "Domingo\n" 
             "Escriba un dia: ").lower()

match dias:
    case "lunes":
        print("Dia 1")
    case "martes":
        print("Dia 2")
    case "miercoles":
        print("Dia 3")
    case "jueves":
        print("Dia 4")
    case "viernes":
        print("Dia 5")
    case "sabado":
        print("Dia 6")
    case "domingo":
        print("Dia 7")
    case _:
        print("Opcion no valida")