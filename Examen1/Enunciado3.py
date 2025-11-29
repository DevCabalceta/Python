# Pide al usuario una calificación (0-100) y muestra:  
# o "Aprobado" si es mayor o igual a 60 
# o "Reprobado" si es menor a 60 
# o "Excelente" si es mayor o igual a 90

calificacion = int(input("Digite una calificación (0-100): "))

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 60:
    print("Aprobado")
else:
    print("Reprobado")