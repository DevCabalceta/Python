import tkinter as tk
from tkinter import ttk

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

boton_agregar = tk.Button(ventana, text="Generar XML", command= agregar_persona)
boton_agregar.pack(pady=10)

tabla = ttk.Treeview(ventana, columns=("nombre", "edad",), show="headings")
tabla.heading("nombre", text="Nombre")
tabla.heading("edad", text="Edad")
tabla.pack(pady=10, fill="both", expand=True)

ventana.mainloop()
