import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

fila = tk.Frame(ventana)
fila.pack(pady=50)

# Labels
label1 = tk.Label(fila, text="Valor 1", font=("Arial", 14))
label1.pack(side="left", padx=15)

label2 = tk.Label(fila, text="Valor 2", font=("Arial", 14))
label2.pack(side="left", padx=15)

# Inputs
fila2 = tk.Frame(ventana)
fila2.pack(pady=50)

input1 = tk.Entry(fila2, font=("Arial", 14))
input1.pack(padx=10, side="left")

input2 = tk.Entry(fila2, font=("Arial", 14))
input2.pack(padx=10, side="left")

# Etiqueta para ver resultado
resultadoLabel = tk.Label(ventana, text="", font=("Arial", 14), fg="blue")
resultadoLabel.pack(pady=10)

def sumar():
    valor1 = int(input1.get())
    valor2 = int(input2.get())
    
    resultadoLabel.config(text=valor1+valor2)

# BotonSumar
botonSumar = tk.Button(ventana, text="Realizar suma", command= sumar)
botonSumar.pack(pady=10)

# Levantar
ventana.mainloop()