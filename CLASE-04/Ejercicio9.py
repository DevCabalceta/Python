# usted tiene un user quemado y un password quemado

while True:

    user = "admin"
    password = "admin123"

    userinput = input("Digite usuario: ")
    passinput = input("Digite password: ")

    if (userinput == user) and (passinput == password):
        print("Entraste al sistema")
        break
    else:
        print("Credenciales incorrectas intente nuevamente")