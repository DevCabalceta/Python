import math as mt

calificaciones = [78, 55, 90, 62, 45, 88, 100, 59, 73, 81]

while True:

    menu = int(input("Bienvenido al Sistema de Notas \n"
                     "1. Mostrar promedio General del grupo \n"
                     "2. Mostrar aprobaciones y reprobaciones \n"
                     "3. Mostrar calificación mas alta del grupo\n"
                     "4. Mostrar calificación mas baja del grupo \n"
                     "5. Mostrar calificación de menor a mayor \n"
                     "6. Salir \n"
                     "Seleccione una opcion: "))
    
    match menu:
        case 1:
            suma = 0
            for c in calificaciones:
                suma = suma + c
                promedio = suma / 10
            print(f"El promedio general del grupo es de: {promedio} \n")
        case 2:
            aprobaron = 0
            reprobaron = 0
            for c in calificaciones:
                if c >= 60:
                    aprobaron = aprobaron + 1
                else:
                    reprobaron = reprobaron + 1

            print(f"Aprobaron: {aprobaron}, Estudiantes \n"
                f"Reprobaron: {reprobaron}, Estudiantes \n")
        case 3:
            alta = max(calificaciones)
            print(f"La calificación mas alta es: {alta} \n")
        case 4:
            baja = min(calificaciones)
            print(f"La calificación mas baja es: {baja} \n")
        case 5:
            orden = sorted(calificaciones)
            print("Calificación de menor a mayor")
            for o in orden:
                print(f"Calificacion: {o}")
        case 6:
            print("Saliendo del Sistema...")
            break
        case __:
            print("Opción incorrecta, seleccione nuevamente.")