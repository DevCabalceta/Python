import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk

def MostrarMensaje():
    ventana_msg = tk.Toplevel()
    ventana_msg.title("Informacion nueva VLA")
    ventana_msg.geometry("350x400")
    ventana_msg.resizable(False, False)

    #fuente
    fuente = font.Font(family="Comic Sans MS", size=12, weight="bold")

    imagen = Image.open(r'C:\Users\Gabriel Cabalceta\Documents\Python\CLASE-13\SeleCostaRica.png')
    imagen = imagen.resize((150,150)) #Ajustar imagen
    image_tk = ImageTk.PhotoImage(imagen)

    lbl_img = tk.Label(ventana_msg, image= image_tk)
    lbl_img.image = image_tk
    lbl_img.pack(pady=20)

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
ventana.title("Ejemplo de tipografia con imagen")

btn = ttk.Button(ventana, text="Mostrar Imagen", command=MostrarMensaje)
btn.pack(pady=20)

ventana.mainloop()
