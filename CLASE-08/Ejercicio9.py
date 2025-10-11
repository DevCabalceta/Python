class Telefonos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def VerDetalleTelefono(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

listaTelefonos = []

while True:
    menu = int(input("1. Agregar Telefono \n"
                     "2. Ver todos los Telefonos\n"
                     "3. Buscar Telefono \n"
                     "4. Salir \n"
                     "Digite opcion: "))
    
    match menu:
        case 1:
            marca = int(input("1. Apple \n"
                              "2. Huawei \n"
                              "3. Samsung \n"
                              "4. Xiaomi \n"
                              "Digite opcion: "))
            match marca:
                case 1:
                    marca = "Apple"
                case 2:
                    marca = "Huawei"
                case 3:
                    marca = "Samsung"
                case 4:
                    marca = "Xiaomi"
                case __:
                    marca = "NA"

            if marca != "NA":
                modelo = input("Digite modelo del telefono: ")
                dispositivo = Telefonos(marca, modelo)
                listaTelefonos.append(dispositivo)
            else:
                print("Lo sentimos pero no existe esa marca seleccionada")
        case 2:
            for disp in listaTelefonos:
                disp.VerDetalleTelefono()
        case 3:
            marca = input("Digite marca del telefono: ")
            modelo = input("Digite modelo del telefono: ")
            bandera = False

            for dist in listaTelefonos:
                if(disp.marca.upper() == marca.upper()) and (disp.modelo.upper() == modelo.upper()):
                    bandera = True
                    break

            if bandera == True:
                disp.VerDetalleTelefono()
            else:
                print("No exite el telefono")                
        case 4:
            print("Saliendo...")
            break
        case __:
            print("Oopcion incorrecta, digite nuevamente")
    
