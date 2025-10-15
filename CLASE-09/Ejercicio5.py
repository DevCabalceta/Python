while True:

    menu = input("Bienvenido al Sistema \n"
                     "A: Voy a despertarme \n"
                     "2: Voy a comer \n"
                     "$: Quiero saludar\n"
                     ".: Quiero salir del sistema \n"
                     "Seleccione una opcion: ").upper()
    
    match menu:
        case "A":
            print("Estoy despertandome")
        case "2":
            print("Estoy comiendo")
        case "$":
            print("Estoy saludando")
        case ".":
            print("Saliendo del sistema...")
            break
        case __:
            print("Opción invalida, digite nuevamente")
    
