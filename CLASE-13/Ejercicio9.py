import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

vector = ["Adolfo", "Dilson", "Gabriel", "Nidia"]

lista = tk.Listbox(ventana)

for nombre in vector:
    lista.insert(tk.END, nombre)

lista.pack()


# Levantar
ventana.mainloop()