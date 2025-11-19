import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("300x300")

def mostrarInfo():
    messagebox.showinfo("Informacion","Esto es un mensaje informativo")

def mostrarWarning():
    messagebox.showwarning("Advertencia","Cuidado con lo que estas haciendo")

def mostrarError():
    messagebox.showerror("Error","Ha ocurrido un error inesperado")

def preguntar_salir():
    respuesta = messagebox.askyesno("Confirmacion", "Desea salir?")
    print("La respuesta de la confirmacion es: ", respuesta)
    if respuesta:
        ventana.destroy()

btn_info = tk.Button(ventana, text="Mostrar Informacion", command=mostrarInfo)
btn_info.pack(pady=10)

btn_warning = tk.Button(ventana, text="Mostrar Warning", command=mostrarWarning)
btn_warning.pack(pady=10)

btn_error = tk.Button(ventana, text="Mostrar Error", command=mostrarError)
btn_error.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir", command=preguntar_salir)
btn_salir.pack(pady=10)

# Levantar
ventana.mainloop()