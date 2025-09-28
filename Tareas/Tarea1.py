# Un banco desea implementar un sistema que clasifique a sus clientes según su edad,
# ingresos mensuales y tipo de cuenta. El sistema debe asignar una categoría de cliente
# y ofrecer beneficios personalizados.


while True:

    menu = int(input("Bienvenido al Sistema Bancario \n"
                     "1. Digitar datos para ver beneficio \n"
                     "2. Salir \n"
                     "Seleccione una opcion: "))
    
    match  menu:
        case 1:
            print("Entrastes al sistema")
            # Datos Usuario
            edad = int(input("Digite su edad: "))
            ingresosMensuales = float(input("Digite sus ingresos mensuales: "))
            tipoCuenta = int(input("1. Ahorro \n"
                                "2. Corriente \n"
                                "3. Premium \n"
                                "Seleccione su tipo de cuenta: "))
            
            match tipoCuenta:
                case 1:
                    if edad < 18 and ingresosMensuales < 1000:
                        print("Tipo cuenta: ahorro \n"
                              "Edad: menor \n"
                              "Ingresos: bajo \n"
                              "Beneficio: Acceso a cuenta educativa sin comisiones \n")
                    elif (edad >= 18 and edad < 60) and ingresosMensuales < 1000:
                        print("Tipo cuenta: ahorro \n"
                              "Edad: adulto \n"
                              "Ingresos: bajo \n"
                              "Beneficio: Programa de ahorros con metas y recompensa \n")
                    elif (edad >= 18 and edad < 60) and (ingresosMensuales >= 1000 and ingresosMensuales <= 5000):
                        print("Tipo cuenta: ahorro \n"
                              "Edad: adulto \n"
                              "Ingresos: medio \n"
                              "Beneficio: Tasa preferencial en ahorro programado \n")
                    elif edad >= 60 and ingresosMensuales > 5000: 
                        print("Tipo cuenta: ahorro \n"
                              "Edad: senior \n"
                              "Ingresos: alto \n"
                              "Beneficio: Bonificacion anual por fidelidad \n")
                    else:
                        print("Lo sentimos, no hay beneficio registrado para su categoría.")               
                case 2:
                    if edad < 18 and (ingresosMensuales >= 1000 and ingresosMensuales <= 5000):
                        print("Tipo cuenta: corriente \n"
                              "Edad: menor \n"
                              "Ingresos: medio \n"
                              "Beneficio: Cuenta supervisada con control parental y educacion financiera \n")
                    elif (edad >= 18 and edad < 60) and ingresosMensuales < 1000:
                        print("Tipo cuenta: corriente \n"
                              "Edad: adulto \n"
                              "Ingresos: bajo \n"
                              "Beneficio: Linea de credito basica y asesoria financiera \n")
                    elif (edad >= 18 and edad < 60) and ingresosMensuales > 5000:
                        print("Tipo cuenta: corriente \n"
                              "Edad: adulto \n"
                              "Ingresos: alto \n"
                              "Beneficio: Tarjeta de debito con cashback y seguros incluidos \n")
                    elif edad >= 60 and (ingresosMensuales >= 1000 and ingresosMensuales <= 5000):
                        print("Tipo cuenta: corriente \n"
                              "Edad: senior \n"
                              "Ingresos: medio \n"
                              "Beneficio: Atencion prioritaria en sucursal y descuentos en servicios \n")
                    else:
                        print("Lo sentimos, no hay beneficio registrado para su categoría.")
                case 3:
                    if edad < 18 and ingresosMensuales > 5000:
                        print("Tipo cuenta: premium \n"
                              "Edad: menor \n"
                              "Ingresos: alto \n"
                              "Beneficio: Cuenta inversion juvenil con tutor financiero \n")
                    elif (edad >= 18 and edad < 60) and ingresosMensuales > 5000:
                        print("Tipo cuenta: premium \n"
                              "Edad: adulto \n"
                              "Ingresos: alto \n"
                              "Beneficio: Asesor financiero personal y linea de inversion exclusiva \n")
                    elif edad >= 60 and ingresosMensuales > 5000:
                        print("Tipo cuenta: premium \n"
                              "Edad: senior \n"
                              "Ingresos: alto \n"
                              "Beneficio: Membresia VIP, viajes bonificados y gestion patrimonial\n")
                    elif (edad >= 18 and edad < 60) and (ingresosMensuales >= 1000 and ingresosMensuales <= 5000):
                        print("Tipo cuenta: premium \n"
                              "Edad: adulto \n"
                              "Ingresos: medio \n"
                              "Beneficio: Acceso a seminarios financieros y beneficios en salud \n")
                    else:
                        print("Lo sentimos, no hay beneficio registrado para su categoría.")
                case _:
                    print("Opcion incorrecta, digite nuevamente")
        case 2:
            print("Saliendo del Sistema")
            break
        case _:
            print("Opcion incorrecta, digite nuevamente")