while True:
    menu = int(input("Bienvenido al Sistema Bancario \n"
                     "1. Digitar datos para ver beneficio \n"
                     "2. Salir \n"
                     "Seleccione una opcion: "))
    
    match menu:
        case 1:
            # === Datos Usuario ===
            edad = int(input("Digite su edad: "))
            ingresos = float(input("Digite sus ingresos mensuales: "))
            tipoCuenta = int(input("1. Ahorro \n"
                                   "2. Corriente \n"
                                   "3. Premium \n"
                                   "Seleccione su tipo de cuenta: "))

            # === Clasificación edad ===
            if edad < 18:
                categoriaEdad = "menor"
            elif edad >= 18 and edad < 60:
                categoriaEdad = "adulto"
            else:
                categoriaEdad = "senior"

            # === Clasificación ingresos ===
            if ingresos < 1000:
                categoriaIngreso = "bajo"
            elif ingresos <= 5000:
                categoriaIngreso = "medio"
            else:
                categoriaIngreso = "alto"

            # === Tipo de cuenta (texto) ===
            match tipoCuenta:
                case 1:
                    cuenta = "ahorro"
                case 2:
                    cuenta = "corriente"
                case 3:
                    cuenta = "premium"
                case _:
                    print("Opción incorrecta")
                    continue  # vuelve al menú principal

            # === Beneficio asignado ===
            match (cuenta, categoriaEdad, categoriaIngreso):
                case ("ahorro", "menor", "bajo"):
                    beneficio = "Acceso a cuenta educativa sin comisiones"
                case ("ahorro", "adulto", "bajo"):
                    beneficio = "Programa de ahorro con metas y recompensas"
                case ("ahorro", "adulto", "medio"):
                    beneficio = "Tasa preferencial en ahorro programado"
                case ("ahorro", "senior", "alto"):
                    beneficio = "Bonificación anual por fidelidad"

                case ("corriente", "menor", "medio"):
                    beneficio = "Cuenta supervisada con control parental y educación financiera"
                case ("corriente", "adulto", "bajo"):
                    beneficio = "Línea de crédito básica y asesoría financiera"
                case ("corriente", "adulto", "alto"):
                    beneficio = "Tarjeta de débito con cashback y seguros incluidos"
                case ("corriente", "senior", "medio"):
                    beneficio = "Atención prioritaria en sucursal y descuentos en servicios"

                case ("premium", "menor", "alto"):
                    beneficio = "Cuenta de inversión juvenil con tutor financiero"
                case ("premium", "adulto", "alto"):
                    beneficio = "Asesor financiero personal y línea de inversión exclusiva"
                case ("premium", "senior", "alto"):
                    beneficio = "Membresía VIP, viajes bonificados y gestión patrimonial"
                case ("premium", "adulto", "medio"):
                    beneficio = "Acceso a seminarios financieros y beneficios en salud"

                case _:
                    beneficio = "Lo sentimos, no hay beneficio registrado para su categoría."

            # === Mostrar resultado ===
            print("\n=== RESULTADO ===")
            print(f"Tipo de cuenta: {cuenta}")
            print(f"Edad: {categoriaEdad}")
            print(f"Ingresos: {categoriaIngreso}")
            print(f"Beneficio: {beneficio}\n")

        case 2:
            print("Saliendo del Sistema")
            break
        case _:
            print("Opción incorrecta, digite nuevamente")
