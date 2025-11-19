import tkinter as tk
from tkinter import font
from tkinter import ttk

def MostrarMensaje():
    ventana_msg = tk.Toplevel()
    ventana_msg.title("Informacion nueva VLA")
    ventana_msg.geometry("350x150")
    ventana_msg.resizable(False, False)

    #fuente
    fuente = font.Font(family="Comic Sans MS", size=12, weight="bold")

    label = tk.Label(
        ventana_msg,
        text=("Este es un mensaje con tipografia aplicada"),
        font=fuente
    )
    label.pack(pady=10)

    boton = ttk.Button(
        ventana_msg,
        text="Aceptar",
        command= ventana_msg.destroy
    )
    boton.pack()


ventana = tk.Tk()
ventana.title("Ejemplo de tipografia")

btn = ttk.Button(ventana, text="Mostrar Mensaje", command=MostrarMensaje)
btn.pack(pady=20)

ventana.mainloop()
