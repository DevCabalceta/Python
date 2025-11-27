import tkinter as tk
from tkinter import ttk

#Ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo con tabla")
ventana.geometry("600x400")

def AgregarPalabra():
    #Captar valor ingresado
    valor = entrada.get()
    tabla.insert("", "end", values=(valor,))
    entrada.delete(0, tk.END)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Agregar", command=AgregarPalabra)
boton.pack(pady=5)

#table crea la tabla, insert en ventana, define las columnas, le indica a tkinder que muestre los encabezados de las columnas
tabla = ttk.Treeview(ventana, columns=("col1",), show="headings")
#Definir los encabezados
tabla.heading("col1", text="Valor ingresado")
#both hace que estire la tabla horizontal y verticalmente, expand = que ocupe el espacio extra cuando la ventana se agranda
tabla.pack(pady=10, fill="both", expand=True)

ventana.mainloop()