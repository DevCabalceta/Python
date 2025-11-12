import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

# Color fondo
ventana.configure(bg="#206c85")

# Variable asociado checkbox (0 no marcado, 1 marcado)
opcionCheck = tk.IntVar()

checkbox = tk.Checkbutton(
    ventana,
    text="Aceptar terminos y condiciones",
    variable=opcionCheck,
    font=("Arial", 14),
    bg="#206c85",
    fg="white",
    selectcolor="#206c85",
    activebackground="#206c85",
    activeforeground="white"
)
checkbox.pack(pady=20)


resultadoLabel = tk.Label(ventana, text="", font=("Arial", 14), fg="white", bg="#206c85")
resultadoLabel.pack(pady=10)

def mostrarEstoTerminosCondiciones():
    if opcionCheck.get() == 1:
        resultadoLabel.config(text="Le dio click")
    else:
        resultadoLabel.config(text="No le dio click")

boton = tk.Button(ventana, text="Ver estado", command= mostrarEstoTerminosCondiciones)
boton.pack(pady=10)

# Levantar
ventana.mainloop()