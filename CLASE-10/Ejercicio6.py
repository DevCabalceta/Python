# Clase puerta 
#     id 
#     abrir 
#     cerrar 
#     estado 

# lista puertas (4 puertas) 

# 1. Abrir puerta
#     cual puerta quiere abrir 
# 2. Cerrar puerta 
#     cual puerta quiero cerrar 
# 3. Ver estado de todas las puertas 

class Puerta:
    def __init__(self, id, abierta):
        self.id = id
        self.abierta = abierta

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def estado(self):
        estado = ""

        if self.abierta== True:
            estado = "abierta"
        else:
            estado = "cerrada"
        
        print(f"Puerta: {self.id}, y esta: {estado}")

listaPuertas = []
puerta1 = Puerta("A31", False)
puerta2 = Puerta("C14", False)
puerta3 = Puerta("D54", False)
puerta4 = Puerta("A1", False)

listaPuertas.append(puerta1)
listaPuertas.append(puerta2)
listaPuertas.append(puerta3)
listaPuertas.append(puerta4)

while True:

    menu = int(input("Bienvenido al Sistema \n"
                     "1. Abrir puerta \n"
                     "2. Cerrar puerta \n"
                     "3. Ver estado de todas las puertas \n"
                     "4. Salir \n"
                     "Seleccione una opcion: "))
    
    match menu:
        case 1:
            puertas = ""

            for puerta in listaPuertas:
                puertas += puerta.id + "\n"

            puertaSeleccionada = input(f"Digite una puerta:\n" + puertas).upper()

            for puerta in listaPuertas:
                if puertaSeleccionada == puerta.id:
                    puerta.abrir()
                    print("Puerta abierta")

        case 2:
            puertas = ""

            for puerta in listaPuertas:
                puertas += puerta.id + "\n"

            puertaSeleccionada = input(f"Digite una puerta:\n" + puertas).upper()

            for puerta in listaPuertas:
                if puertaSeleccionada == puerta.id:
                    puerta.cerrar()
                    print("Puerta cerrada")
        case 3:
            for puerta in listaPuertas:
                puerta.estado()
        case 4:
            print("Saliendo del Sistema...")
            break
        case __:
            print("Opción incorrecta, seleccione nuevamente.")

