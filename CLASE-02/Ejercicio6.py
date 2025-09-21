# bolean
# Mujer es verdadero = true 
# Hombre es falso = false 

# sexoPersona = True
# sexoPersonaTexto = int(input("Digite 1.Hombre 2.Mujer: "))

# if sexoPersonaTexto == 1:
#     sexoPersona = False
# else:
#     sexoPersona = True

# print("El valor de sexo de la persona es: ", sexoPersona)

sexoPersona = input("Digite el sexo de la persona (mujer, hombre): ")

es_mujer = sexoPersona == "mujer"

print ("El resultado es: ", es_mujer)