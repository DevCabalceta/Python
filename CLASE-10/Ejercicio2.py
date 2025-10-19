# numeros = [56,35,90,100,21,78]
# Ordene de menor a mayor
# De usar cuantos vectores considere, si quiere usar funciones
# 21, 35, 56,78, 90, 100
# ordenamiento sort



numeros = [56,35,90,100,21,78]
n = len(numeros) # 6 veces
for i in range(n):
    print("Estamos en la vuelta:", i, "del primer for")
    for j in range(n-1):
        if numeros[j] > numeros[j+1]:
            temporal = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = temporal

print(numeros)
