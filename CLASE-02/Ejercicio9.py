# Pida un usuario
# Pida una contraseña
# Si ambos valor es admin123 y la contraseña es 12345678 
# Puede ingresar al sistema, usted esta logueado
# No puede entrar
# El resultado final le tengo que si calza o no

banderaIngreso = True
user = input("Digite el usuario: ")

if user == "admin123":
    password = input("Digite la contraseña: ")
    if password == "12345678":
        banderaIngreso = True
    else:
        banderaIngreso = False
else:
    banderaIngreso = False

if(banderaIngreso == True):
    print("Felicidades, logrstes ingresar")
else:
    print("Lo siento, revisa las credenciales")