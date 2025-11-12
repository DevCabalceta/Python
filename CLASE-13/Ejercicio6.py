import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")

opciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]
combo = ttk.Combobox(ventana, values=opciones, font=("Arial", 14))
combo.pack(pady=10)

# Colocar un valor por defecto
combo.current(0)

# Inputs
fila1 = tk.Frame(ventana)
fila1.pack(pady=50)

input1 = tk.Entry(fila1, font=("Arial", 14))
input1.pack(padx=10, side="left")

input2 = tk.Entry(fila1, font=("Arial", 14))
input2.pack(padx=10, side="left")

# Resultado
resultadoLabel = tk.Label(ventana, text="", font=("Arial", 14), fg="blue")
resultadoLabel.pack(pady=10)

def RealizarOperacion():
    valorCombo = combo.get()
    valor1 = float(input1.get())
    valor2 = float(input2.get())

    match(valorCombo):
        case "Sumar":
            resultadoLabel.config(text=(valor1 + valor2))
        case "Restar":
            resultadoLabel.config(text=(valor1 - valor2))
        case "Multiplicar":
            resultadoLabel.config(text=(valor1 * valor2))
        case "Dividir":
            if valor2 != 0:
                resultadoLabel.config(text=(valor1 / valor2))
            else:
                resultadoLabel.config(text="Error: División por cero")

# BotonSumar
botonMostrar = tk.Button(ventana, text="Resultado", command= RealizarOperacion)
botonMostrar.pack(pady=10)

# Levantar
ventana.mainloop()