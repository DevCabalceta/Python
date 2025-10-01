personas = []

while True:
    menu = int(input("Bienvenido al Sistema \n"
                     "1. Agregar Persona \n"
                     "2. Ver Personas \n"
                     "3. Salir \n"
                     "Seleccione una opcion: "))
    
    match menu:
        case 1:
            contador = int(input("Digite cantidad de personas a ingresar: "))
            for i in range(contador):
                nombre = input("Digite un nombre: ")
                if nombre == "":
                    print("No ingresastes ningun nombre")
                else:
                    personas.append(nombre)
        case 2:
            for p in personas:
                print("El nombre insertado es: ", p)
        case 3:
            print("Saliendo del Sistema")
            break
        case _:
            print("Opción incorrecta, digite nuevamente")

