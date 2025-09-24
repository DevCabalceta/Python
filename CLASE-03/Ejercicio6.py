# Digite un numero del 1 al 5
# Diga cual fue el numero que digito pero con letra

opcion = input("Escriba un numero del 1 al 5: ")

match opcion:
    case "1":
        print("Usted digito el numero uno")
    case "2":
        print("Usted digito el numero dos")
    case "3":
        print("Usted digito el numero tres")
    case "4":
        print("Usted digito el numero cuatro")
    case "5":
        print("Usted digito el numero cinco")
    case _:
        print("Opcion no valida")