import tkinter as tk

#===================================
#  Manejo de la ventana
#===================================
ventana = tk.Tk()
ventana.title("Ejemplo con tabla")
ventana.geometry("300x200")

def ocultar_todo():
    label.pack_forget()
    boton_saludo.pack_forget()
    boton_mostrar.pack()

def mostrar_todo():
    label.pack(pady=10)
    boton_saludo.pack(pady=5)
    boton_mostrar.pack_forget()

label = tk.Label(ventana, text="Hola soy un texto visible")
label.pack(pady=10)

boton_saludo = tk.Button(ventana, text="Soy boton")
boton_saludo.pack(pady=5)

boton_ocultar = tk.Button(ventana, text="Ocultar Label y Boton", command=ocultar_todo)
boton_ocultar.pack(pady=5)

boton_mostrar = tk.Button(ventana, text="Mostrar Label y Boton", command=mostrar_todo)
boton_mostrar.pack_forget()

ventana.mainloop()