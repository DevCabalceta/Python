import xml.etree.ElementTree as ET

listaPersonas = []

class Persona:
    def __init__(self, nombre, apellido,cuentas):
        self.nombre = nombre
        self.apellido = apellido
        self.cuentas = cuentas

    def ObtenerSaldoAFavor(self):
        total = 0
        for cuenta in self.cuentas:
            total = total + cuenta.saldoAFavor
        
        return total
    
    def ObtenerSaldoABloqueado(self):
        total = 0
        for cuenta in self.cuentas:
            total = total + cuenta.saldoBloqueado
        
        return total

class Cuentas:
    def __init__(self, saldoAFavor, saldoBloqueado):
        self.saldoAFavor = saldoAFavor
        self.saldoBloqueado = saldoBloqueado

arbol = ET.parse("Ejemplo1.xml")
root = arbol.getroot()

for nodoPersona in root.findall("Persona"):
    nombre = nodoPersona.find("nombre").text
    apellido = nodoPersona.find("apellido").text

    listaCuentas = []

    for nodoCuenta in nodoPersona.find("cuentas").findall("cuenta"):
        saldoAFavor = float(nodoCuenta.find("saldoAFavor").text)
        saldoBloqueado = float(nodoCuenta.find("saldoBloqueado").text)

        cuenta = Cuentas(saldoAFavor, saldoBloqueado)
        listaCuentas.append(cuenta)

    persona = Persona(nombre, apellido, listaCuentas)
    listaPersonas.append(persona)

for persona in listaPersonas:
    print("Persona:",persona.nombre,persona.apellido, " - Saldo a Favor:", persona.ObtenerSaldoAFavor() )
