import tkinter as tk
from tkinter import messagebox
from tkinter import font

def mostrarMensaje():
    messagebox.showinfo("Informacion",
                        "Este es un mensaje con la tipografia aplicada en la ventana")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title = "Ejemplo de tipografia"
ventana.geometry("300x300")


mi_fuente = ("Comic Sans Ms", 16, "bold")

label = tk.Label(ventana, text="Hola con tipografia", font=mi_fuente)
label.pack(pady=20)

boton = tk.Button(
    ventana,
    text="Mostrar Mensaje",
    font=mi_fuente,
    command=mostrarMensaje
)
boton.pack()

# Levantar
ventana.mainloop()