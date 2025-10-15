#Variables
descuento = 0
cantidadProducto = 20
montoOriginal = 100000
totalPagarFinal = 0

#Opcion 1
if cantidadProducto <= 20:
    descuento = 0.03
elif cantidadProducto <= 40:
    descuento = 0.04
else:
    descuento = 0.06

totalPagarFinal = montoOriginal - (montoOriginal*descuento)
print(f"El total a pagar es: {totalPagarFinal}")


#Opcion 2
match cantidadProducto:
    case cantidadProducto if cantidadProducto <= 20:
        descuento = 0.03
    case cantidadProducto if cantidadProducto <= 40:
        descuento = 0.04
    case cantidadProducto if cantidadProducto <= 60:
        descuento = 0.06

totalPagarFinal = montoOriginal - (montoOriginal*descuento)
print(f"El total a pagar es: {totalPagarFinal}")
