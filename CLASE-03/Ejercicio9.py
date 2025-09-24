nota = float(input("Digite la nota: "))

match nota:
    case _ if nota <= 40:
        print("Debe repetir el curso")
    case _ if 41 <= nota <=69:
        print("Debe ir a ampliacion")
    case _ if nota >= 70:
        print("Aprobado")
    case _:
        print("Opcion no valida")