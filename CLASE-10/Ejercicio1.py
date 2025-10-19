# definir una clase estudiantes
#      nombre
#      edad
#      promedio
# Dentro de la clase usted va a crear una funcion que sea esAprobado() que va a devolver true si 
# el promedio es mayor que sea >=, si no false
# Crear una funcion que cargue el vector, pida cuantos estudiantes quiere ingresar
# Mostrar los estudiantes aprobados
# Mostrar el promedio general del curso

class Estudiante:
    nombre = ""
    edad = 0
    promedio = 0.0

    def esAprobado(self):
        if self.promedio >= 70:
            return True
        else:
            return False


def cargarEstudiantes():
    estudiantes = []
    cantidad = int(input("Digite la cantidad de estudiantes a registrar: "))

    for numeroEstudiante in range(cantidad):
        estudiante = Estudiante()
        estudiante.nombre = input("Digite el nombre: ")
        estudiante.edad = int(input("Digite la edad: "))
        estudiante.promedio = float(input("Digite el promedio: "))
        estudiantes.append(estudiante)

    return estudiantes


def mostrarAprobados(vectorEstudiantes):
    print("\nEstudiantes Aprobados: ")

    for e in vectorEstudiantes:
        if e.esAprobado() == True:
            print(f"Estudiante: {e.nombre} \n"
                  f"Edad: {e.edad} \n"
                  f"Promedio: {e.promedio} \n\n")
            
def promedioGeneral(vectorEstudiantes):

    promedioGrupo = 0
    for j in vectorEstudiantes:
        promedioGrupo = promedioGrupo + j.promedio

    return promedioGrupo/ len(vectorEstudiantes)

listaEstudiantes = cargarEstudiantes()
mostrarAprobados(listaEstudiantes)
promedio = promedioGeneral(listaEstudiantes)
print(f"Promedio general del curso es: {promedio}")