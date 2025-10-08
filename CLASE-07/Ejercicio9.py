
def PedirDatos():
    vectorPersonas = []
    for i in range(4):
        persona = input("Digite nombre de persona: ")
        vectorPersonas.append(persona)
    return vectorPersonas

def MostrarDatos(vectorP):
    for p in personas:
        print(f"Persona: {p}")

personas = PedirDatos()
MostrarDatos(personas)
