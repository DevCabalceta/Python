tipoTarjeta = input("Con que tarjeta va a pagar Visa Mastercard American: ").lower()
totalPagar = float(input("Cuanto va a pagar: "))
descuento = 0

if tipoTarjeta == "visa":
    descuento = totalPagar * 0.05
elif tipoTarjeta == "mastercard":
    descuento = totalPagar * 0.1
elif tipoTarjeta == "american":
    descuento = totalPagar * 0.07
else:
    descuento = 0

print("El descuento aplicado es de: ", descuento, " y el total a pagar es de: ", (totalPagar-descuento))