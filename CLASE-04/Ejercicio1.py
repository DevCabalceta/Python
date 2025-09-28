# 3 variables
# temperatura int 
# humedad int 
# viento int 

# soleado y seco

temperatura = 30
humedad = 20
viento = 10

match (temperatura, humedad, viento):
    case (t,h,v) if t>=30 and h<40 and v>=10:
        print("Soleado y seco")
    case (t,h,v) if t>30 and h>60:
        print("Humedo y caluroso")
    case (t,h,v) if (t>100 and h>80) or v>120:
        print("Nos vamos a morir todos")
    case _:
        print("Condiciones no contempladas")