
personas = ["Ana", "Luis", "Carlos", "Elena", "Luis", "Adolfo"]
personasNuevas = []

for i in range (len(personas)):
    if personas[i]!="Luis":
        personasNuevas.append(personas[i])

for p in range (len(personasNuevas)):
    print("Persona: ", personasNuevas[p])


