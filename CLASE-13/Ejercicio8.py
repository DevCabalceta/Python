import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

# Variable compartida entre los radios
opcionSeleccionada = tk.StringVar()
opcionSeleccionada.set("Opcion 1") #Valor por defecto

radio1 = tk.Radiobutton(
    ventana,
    text = "Opcion 1",
    variable = opcionSeleccionada,
    value = "Opcion 1"
)
radio1.pack(pady=5)

radio2 = tk.Radiobutton(
    ventana,
    text = "Opcion 2",
    variable = opcionSeleccionada,
    value = "Opcion 2"
)
radio2.pack(pady=5)

resultadoLabel = tk.Label(ventana, text="", font=("Arial", 14), fg="black")
resultadoLabel.pack(pady=10)

def MostrarSeleccionado():
    if opcionSeleccionada.get() == "Opcion 1":
        resultadoLabel.config(text="Valor seleccionado 1")
    else:
        resultadoLabel.config(text="Valor seleccionado 2")

boton = tk.Button(ventana, text="Ver estado", command= MostrarSeleccionado)
boton.pack(pady=10)


# Levantar
ventana.mainloop()