import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

# Etiqueta label
etiquetaLabel = tk.Label(ventana, text="Inserte un numero", font=("Arial",14))
etiquetaLabel.pack(pady=20)

# Etiqueta Input
input1 = tk.Entry(ventana, font=("Arial", 14))
input1.pack(pady=10)

# Etiqueta para ver resultado
resultadoLabel = tk.Label(ventana, text="", font=("Arial", 14), fg="blue")
resultadoLabel.pack(pady=10)

def mostrarPalabra():
    palabra = input1.get() #Asi se obtiene el texto
    resultadoLabel.config(text=palabra)

# BotonMostrar
botonMostrar = tk.Button(ventana, text="Mostrar Palabra", command= mostrarPalabra)
botonMostrar.pack(pady=10)

# Boton
boton1 = tk.Button(ventana, text="Cerrar ventana", command= ventana.destroy)
boton1.pack(pady=10)

#Levantar
ventana.mainloop()