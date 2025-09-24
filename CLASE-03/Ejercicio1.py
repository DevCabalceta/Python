# Imaginese que tiene una tarjeta de credito 1. Visa 2. Mastercard 3. American
# Variable que sea totalPagar 
# Dependiendo de la tarjeta hay un descuento 1. 5% 2. 10% 3. 7% 
# Mostrar el total de descuento aplicado
# Solicitar al usuario un numero o visa, mastercard o american
# Todo lo que ingresa por el teclado es un string 123

tipoTarjeta = input("Con que tarjeta va a pagar 1=Visa 2=Mastercard 3=American: ")
totalPagar = float(input("Cuanto va a pagar: "))
descuento = 0

if tipoTarjeta == "1":
    descuento = totalPagar * 0.05
elif tipoTarjeta == "2":
    descuento = totalPagar * 0.1
elif tipoTarjeta == "3":
    descuento = totalPagar * 0.07
else:
    descuento = 0

print("El total del descuento es de: ", descuento)