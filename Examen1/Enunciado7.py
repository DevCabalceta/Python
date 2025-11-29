# Crea una clase CuentaBancaria con atributos titular y saldo. Agrega métodos 
# depositar(monto) y retirar(monto). Crea dos cuentas y simula una transferencia 
# entre ellas.


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto} realizado correctamente.")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado correctamente.")
        else:
            print("Fondos insuficientes o monto inválido.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo actual: {self.saldo}")


cuenta1 = CuentaBancaria("Gabriel", 1000)
cuenta2 = CuentaBancaria("Rodolfo", 500)

print("Saldos iniciales:")
cuenta1.mostrar_saldo()
cuenta2.mostrar_saldo()


monto_transferencia = 300
print(f"\nTransferencia de {monto_transferencia} de {cuenta1.titular} a {cuenta2.titular}:")

cuenta1.retirar(monto_transferencia)
cuenta2.depositar(monto_transferencia)

print("\nSaldos después de la transferencia:")
cuenta1.mostrar_saldo()
cuenta2.mostrar_saldo()
