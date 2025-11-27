import tkinter as tk
from tkinter import ttk
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
#  Funcion Cargar XML
#===================================
def cargar_xml():
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

boton_agregar = tk.Button(ventana, text="Cargar XML", command= cargar_xml)
boton_agregar.pack(pady=10)

tabla = ttk.Treeview(ventana, columns=("nombre", "edad",), show="headings")
tabla.heading("nombre", text="Nombre")
tabla.heading("edad", text="Edad")
tabla.pack(pady=10, fill="both", expand=True)

ventana.mainloop()