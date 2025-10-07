# Pilotando un avion 
# 100km al norte 
# 600km al oeste 
# 70km al suroeste 
# 1000km oeste 
# Cuantos km recorrio el avion

direccionVuelo1 = [100,600,70,1000]

cantidadkm = 0

for i in range (len(direccionVuelo1)):
    cantidadkm = cantidadkm + direccionVuelo1[i]
    print(f"Usted recorrio {cantidadkm}km")