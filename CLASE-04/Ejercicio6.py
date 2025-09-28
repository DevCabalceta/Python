

while True:

    menu = int(input("1. Saludar\n" 
                "2. Comer\n" 
                "3. Dormir\n" 
                "4. Caminar\n"
                "5. Salir\n\n"
                "Digite una opcion: "))

    match menu:
        case 1:
            print("Esta saludando")
        case 2:
            print("Esta comiendo")
        case 3:
            print("Esta durmiendo")
        case 4:
            print("Esta caminando")
        case 5:
            print("Esta saliendo del menu")
            break
        case _:
            print("Opcion incorrecta")

