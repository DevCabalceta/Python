class OperacionMatematica:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def Sumar(self):
        print(f"La suma es: {self.val1 + self.val2}")

    def Restar(self):
        print(f"La resta es: {self.val1 - self.val2}")

    def Multiplicar(self):
        print(f"La multiplicacion es: {self.val1 * self.val2}")

    def Division(self):
        print(f"La diviion es: {self.val1 / self.val2}")

numero1 = float(input("Digite el primer valor: "))
numero2 = float(input("Digite el segundo valor: "))
operaciones = OperacionMatematica(numero1, numero2)
operaciones.Sumar()
operaciones.Restar()
operaciones.Multiplicar()
operaciones.Division()