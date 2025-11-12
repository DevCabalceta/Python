import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

opciones = ["Opcion 1", "Opcion 2", "Opcion 3"]
combo = ttk.Combobox(ventana, values=opciones, font=("Arial", 14))
combo.pack(pady=10)

#Colocar un valor por defecto
combo.current(0)

# Levantar
ventana.mainloop()