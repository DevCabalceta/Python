class Institucion:

    def verTodaLaInformacion(self):
        print(f"Nombre: {self.nombre}, Telefono: {self.telefono}, Ubicacion: {self.ubicacion}")

insti1 = Institucion()
nombreInsti = input("Digite el nombre de la institucion: ").upper()
telefonoInsti = input("Digite el telefono de la institucion: ")
ubicacionInsti = input("Digite la ubicacion de la institucion: ")
insti1.nombre = nombreInsti
insti1.telefono = telefonoInsti
insti1.ubicacion = ubicacionInsti
insti1.verTodaLaInformacion()
