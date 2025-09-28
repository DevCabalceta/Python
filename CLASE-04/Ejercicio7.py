# Numero secreto
# en while usted va a pedir un numero
# si el numero ingresado == numero secreto, imprima que le atino al numero y salgase del while 
# caso contrario, siempre vuelva a preguntar por un numero y preguntele si calza con el secreto

while True:

    numeroSecreto = int(input("Digite numero secreto: "))
    numeroAleatorio = 0

    if numeroSecreto == numeroAleatorio:
        print("BINGO")
        break
    else:
        print("Fallastes intente nuevamente")
    