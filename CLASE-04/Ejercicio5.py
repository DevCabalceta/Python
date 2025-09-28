# Pedir un numero al usuario 1.Saludar 2.Comer 3.Dormir 4.Caminar 5.Salir 
# Segun la seleccion, muestre en un print que quiso hacer el usuario 
# solo use if, elif


menu = 0

while menu != 5:
    menu = int(input("1. Saludar\n" 
                "2. Comer\n" 
                "3. Dormir\n" 
                "4. Caminar\n"
                "5. Salir\n\n"
                "Digite una opcion: "))
    if menu == 1:
        print("Esta saludando")
    elif menu == 2:
        print("Esta comiendo")
    elif menu == 3:
        print("Esta durmiendo")
    elif menu == 4:
        print("Esta caminando")
    elif menu == 5:
        print("Esta saliendo del menu")
    else:
        print("Opcion incorrecta")
