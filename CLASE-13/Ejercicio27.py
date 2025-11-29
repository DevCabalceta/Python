import tkinter as tk
from tkinter import ttk
import time

def iniciar_progreso():
    progreso["value"] = 0
    ventana.update_idletasks()

    for i in range(101):
        progreso["value"] = i
        ventana.update_idletasks()
        time.sleep(0.03)

ventana= tk.Tk()
ventana.title("Ventana de progress bar")
ventana.geometry("300x150")

#Crear la barra de progreso
progreso = ttk.Progressbar(
    ventana,
    length=250,
    mode="determinate"
)
progreso.pack(pady=20)

btn = tk.Button(ventana, text="Iniciar", command=iniciar_progreso)
btn.pack()

ventana.mainloop()