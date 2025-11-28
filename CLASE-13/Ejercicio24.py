
import tkinter as tk

ventana= tk.Tk()
ventana.title("Frames organizados")

#frame superior
frameSuperior = tk.Frame(ventana, bg="lightgray", pady=10)
frameSuperior.pack(fill="x")

label1 = tk.Label(frameSuperior, text="Frame Superior")
label1.pack()

#frame inferior
frameInferior = tk.Frame(ventana, bg="lightgreen", pady=10)
frameInferior.pack(fill="both", expand=True)

label2 = tk.Label(frameInferior, text="Frame Inferior")
label2.pack()

ventana.mainloop()