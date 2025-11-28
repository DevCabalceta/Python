class Persona:
    def __init__(self, nombre, apellido, edad, cursos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cursos = cursos

class Curso:
    def __init__(self, nombreCurso, horario):
        self.nombreCurso = nombreCurso
        self.horario = horario

listaPersonas = []
listaCursosVLA = []
curso1 = Curso("Python Fundamentals", "KJ")
curso2 = Curso("SQL", "LM")
curso3 = Curso("Frontend Developer", "VN")
curso4 = Curso("Power BI", "SI")

listaCursosVLA.append(curso1)
listaCursosVLA.append(curso2)
listaCursosVLA.append(curso3)
listaCursosVLA.append(curso4)

listaCursosAri = []
listaCursosAri.append(curso1)
listaCursosAri.append(curso2)
listaCursosAri.append(curso3)
personaAri = Persona("Ari", "Olmos", 25, listaCursosAri)

listaCursosYose = []
listaCursosYose.append(curso3)
personaYose = Persona("Yose", "Astua", 20, listaCursosYose)

listaCursosMadeline = []
listaCursosMadeline.append(curso1)
listaCursosMadeline.append(curso2)
listaCursosMadeline.append(curso3)
listaCursosMadeline.append(curso4)
personaMadeline = Persona("Madeline", "Castro", 22, listaCursosMadeline)

listaPersonas.append(personaAri)
listaPersonas.append(personaYose)
listaPersonas.append(personaMadeline)

for persona in listaPersonas:
    print(f"Persona: {persona.nombre} {persona.apellido} - {persona.edad}")
    print("Los cursos que esta llevando son:")
    for curso in persona.cursos:
        print(f"   {curso.nombreCurso} - {curso.horario}")
    print("------------------------------")