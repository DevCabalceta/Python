
personas = []

while True:
    menu = int(input("Bienvenido al Sistema \n"
                     "1. Agregar Persona \n"
                     "2. Ver Personas \n"
                     "3. Salir \n"
                     "Seleccione una opcion: "))
    
    match menu:
        case 1:
            nombre = input("Digite un nombre: ")
            if nombre == "":
                print("No ingresastes ningun nombre")
            else:
                personas.append(nombre)
        case 2:
            for i in range (len(personas)):
                print("El nombre insertado es: ", personas[i])
        case 3:
            print("Saliendo del Sistema")
            break
        case _:
            print("Opción incorrecta, digite nuevamente")
