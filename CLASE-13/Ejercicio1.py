import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

# Etiqueta label
etiquetaLabel = tk.Label(ventana, text="Mi primer label", font=("Arial",14))
etiquetaLabel.pack(pady=20)

# Boton
boton1 = tk.Button(ventana, text="Cerrar ventana", command= ventana.destroy)
boton1.pack()

#Levantar
ventana.mainloop()