# Pida un usuario
# Pida una contraseña
# Si ambos valor es admin123 y la contraseña es 12345678 
# Puede ingresar al sistema, usted esta logueado
# No puede entrar
# El resultado final le tengo que si calza o no

user = input("Digite el usuario: ")

if user == "admin123":
    password = input("Digite la contraseña: ")
    if password == "12345678":
        print("Estrastes al sistema, sos el administrador")
    else:
        print("La contraseña es incorrecta, no puedes entrar")
else:
    print("El usuario es incorrecto, no puedes entrar")