# Quiero saber que ocupo para ser presidente en costa rica
# Ser costarricense por nacimiento
# Ser del estado seglar
# Tener mas de 30 anios
#Pidale al usuario esos datos y verifique si aplica para ser el proximo presidente
# 1. SI 2. NO
#Haga un print que diga si soy candidato o no
siSoyCostarricense = 1
soyEstadoSeglar = 2
miEdad = 33

#OPCION 1
if siSoyCostarricense == 1:
    if soyEstadoSeglar == 2:
        if miEdad >=30:
            print("Soy candidato a la presidencia")
        else:
            print("No puede ser candidato por la edad")
    else:
        print("No puede ser candidato porque es del estado seglar")
else:
    print("No puede porque no es costarricense")

#OPCION 2
if siSoyCostarricense == 1 and soyEstadoSeglar == 2 and miEdad>=30:
    print("Soy candidato a la presidencia")
else:
    print("No puede ser candidato a la presidencia")

#OPCION 3
match (siSoyCostarricense,soyEstadoSeglar,miEdad >=30):
    case (1,2,True):
        print("Soy candidato a la presidencia")
    case (1,2,False):
        print("No puede ser candidato por la edad")
    case (1,1,_):
        print("No puede ser candidato porque es del estado seglar")
    case (2,_,_):
        print("No puede porque no es costarricense")