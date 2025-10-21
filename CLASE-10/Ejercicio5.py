# Clase Foco un atributo que es encendido TRUE o es FALSE 
# Metodo encender, apagar, estadoFoco 
# Crear 2 objetos de tipo foco
# Encender uno y el otro va a apagar
# Mostrar estado de cada foco

class Foco:
    encendido = False

    def encender(self):
        self.encendido = True
        
    def apagar(self):
        self.encendido = False
        
    def estado(self):
        if self.encendido == True:
            print("El foco esta encendido")
        else:
            print("El foco esta apagado")
        
foco1 = Foco()
foco1.estado()
foco1.encender()
foco1.estado()
foco1.apagar()
foco1.estado()