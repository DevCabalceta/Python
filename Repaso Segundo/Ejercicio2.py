class Persona:
    def __init__(self, nombre, apellido, cuentas):
        self.nombre = nombre
        self.apellido = apellido
        self.cuentas = cuentas

    def ObtenerSaldoAFavor(self):
        total = 0
        for cuenta in self.cuentas:
            total = total + cuenta.saldoAFavor

        return total
    
    def ObtenerSaldoBloqueado(self):
        total = 0
        for cuenta in self.cuentas:
            total = total + cuenta.saldoBloqueado

        return total

class Cuentas:
    def __init__(self, saldoAFavor, saldoBloqueado):
        self.saldoAFavor = saldoAFavor
        self.saldoBloqueado = saldoBloqueado

listaPersonas = []

listaCuentasAri = []
Cuenta1Ari = Cuentas(1000, 50)
Cuenta2Ari = Cuentas(9000, 500)
Cuenta3Ari = Cuentas(100, 800)
listaCuentasAri.append(Cuenta1Ari)
listaCuentasAri.append(Cuenta2Ari)
listaCuentasAri.append(Cuenta3Ari)
personaAri = Persona("Ari", "Olmos", listaCuentasAri)

listaCuentasYos = []
Cuenta1Yos = Cuentas(100, 50)
Cuenta2Yos = Cuentas(100, 10)
Cuenta3Yos = Cuentas(100, 200)
listaCuentasYos.append(Cuenta1Yos)
listaCuentasYos.append(Cuenta2Yos)
listaCuentasYos.append(Cuenta3Yos)
personaYos = Persona("Yos", "Astua", listaCuentasYos)

listaCuentasMadeline = []
Cuenta1Madeline = Cuentas(1500, 0)
Cuenta2Madeline = Cuentas(2000, 0)
Cuenta3Madeline = Cuentas(3000, 0)
listaCuentasMadeline.append(Cuenta1Madeline)
listaCuentasMadeline.append(Cuenta2Madeline)
listaCuentasMadeline.append(Cuenta3Madeline)
personaMadeline = Persona("Madeline", "Castro", listaCuentasMadeline)

listaPersonas.append(personaAri)
listaPersonas.append(personaYos)
listaPersonas.append(personaMadeline)

for persona in listaPersonas:
    print(f"Persona: {persona.nombre} {persona.apellido} - Saldo a Favor: {persona.ObtenerSaldoAFavor()}")
