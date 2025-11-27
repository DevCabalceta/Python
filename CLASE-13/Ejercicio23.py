import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo pequeño de frames")
ventana.geometry("300x150")

#Crear un frame
frame = tk.Frame(ventana, bg="lightblue", padx=10, pady=10)
frame.pack(pady=20)

#Widgets a ese frame
label = tk.Label(frame, text="Hola desde el frame")
label.pack(pady=5)

boton = tk.Button(ventana, text="Click aqui")
boton.pack(pady=5)

ventana.mainloop()