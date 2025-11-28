
import tkinter as tk

ventana= tk.Tk()
ventana.title("Frames organizados")

#frame A
frameA= tk.Frame(ventana, bg="lightgray", pady=20, padx=10)
frameA.pack(fill="y", side="left")

label1 = tk.Label(frameA, text="Frame A")
label1.pack()

#frame B
frameB = tk.Frame(ventana, bg="lightgreen", width=200, height=100)
frameB.pack(fill="y",side="left")

label2 = tk.Label(frameB, text="Frame B")
label2.pack()

#frame C
frameC= tk.Frame(ventana, bg="lightgray",  height=150)
frameC.pack(fill="both", side="top", expand=True)

label3 = tk.Label(frameC, text="Frame C")
label3.pack()

ventana.mainloop()