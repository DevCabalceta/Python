import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import xml.etree.ElementTree as ET

#===================================
#  Clase persona
#===================================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#===================================
#  Funcion para agregar una persona
#===================================
def agregar_persona():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    persona = Persona(nombre, edad)

    tabla.insert("", "end", values=(persona.nombre, persona.edad))

    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)

#===================================
#  Funcion Generar XML
#===================================
def generar_xml():
    root = ET.Element("Personas")

    #recorrer las filas de una tabla
    for item in tabla.get_children():
        valores = tabla.item(item, "values")

        persona_element = ET.SubElement(root, "Persona")
        ET.SubElement(persona_element, "nombre").text = valores[0]
        ET.SubElement(persona_element, "edad").text = valores[1]

    #Crear el arbol
    arbol = ET.ElementTree(root)
    arbol.write("personas.xml", encoding="utf-8", xml_declaration=True)

#===================================
#  Funcion Cargar XML
#===================================
def cargar_xml():

    ruta = filedialog.askopenfilename(
        title="Seleccione el archivo xml",
        filetypes=[("Archivos XML", "*.xml"), ("Todos los archivos", "*.*")]
    )

    #si el usuario cancela, no debe hacer nada
    if not ruta:
        return

    try:
        tree = ET.parse(r'C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-13\personas.xml')
        root = tree.getroot()

        #Limpiar la tabla antes de cargar
        for item in tabla.get_children():
            tabla.delete(item)

        #leer cada persona del xml ya cargado
        for persona_element in root.findall("Persona"):
            nombre = persona_element.find("nombre").text
            edad = persona_element.find("edad").text

            tabla.insert("", "end", values=(nombre, edad))

    except Exception:
        print("No se pudo cargar el archivo")

#===================================
#  Funcion para Eliminar una persona
#===================================
def eliminar_seleccion():
    item = tabla.selection()
    if item:
        tabla.delete(item)

#===================================
#  Eliminar por nombre
#===================================
def eliminar_por_nombre():
    nombreBuscar = entrada_eliminar.get()

    if not nombreBuscar:
        return
    
    for item in tabla.get_children():
        valores = tabla.item(item, "values")
        nombre = valores[0]

        if nombre.lower() == nombreBuscar.lower():
            tabla.delete(item)
            break

        entrada_eliminar.delete(0, tk.END)

#===================================
#  Manejo de la ventana
#===================================
ventana = tk.Tk()
ventana.title("Ejemplo con tabla")
ventana.geometry("600x400")

tk.Label(ventana, text="Nombre").pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Edad").pack(pady=5)
entrada_edad = tk.Entry(ventana, width=40)
entrada_edad.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar Persona a Tabla", command= agregar_persona)
boton_agregar.pack(pady=10)

boton_generar = tk.Button(ventana, text="Generar XML", command= generar_xml)
boton_generar.pack(pady=10)

boton_cargar = tk.Button(ventana, text="Cargar XML", command= cargar_xml)
boton_cargar.pack(pady=10)

tk.Label(ventana, text="Eliminar por nombre").pack(pady=5)
entrada_eliminar = tk.Entry(ventana, width=40)
entrada_eliminar.pack(pady=5)

boton_eliminar_por_nombre = tk.Button(ventana, text="Eliminar Por Nombre", command= eliminar_por_nombre)
boton_eliminar_por_nombre.pack(pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar Seleccionado", command= eliminar_seleccion)
boton_eliminar.pack(pady=10)

tabla = ttk.Treeview(ventana, columns=("nombre", "edad",), show="headings")
tabla.heading("nombre", text="Nombre")
tabla.heading("edad", text="Edad")
tabla.pack(pady=10, fill="both", expand=True)

ventana.mainloop()