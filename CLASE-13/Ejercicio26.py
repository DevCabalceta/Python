import tkinter as tk

ventana= tk.Tk()

#====================Frame A============================
frameA = tk.Frame(ventana, bg="lightgray", pady=20, padx=10, width=150, height=150)
frameA.grid(row=0, column=0, sticky="nsew")
frameA.grid_propagate(False)

label1 = tk.Label(frameA, text="Frame A")
label1.pack()

#====================Frame B============================
frameB = tk.Frame(ventana, bg="lightgray", pady=20, padx=10, width=150, height=150)
frameB.grid(row=0, column=1, sticky="nsew")
frameB.grid_propagate(False)

label2 = tk.Label(frameB, text="Frame B")
label2.pack()

#====================Frame C============================
frameC = tk.Frame(ventana, bg="lightgray", pady=20, padx=10, height=150)
frameC.grid(row=1, column=0, columnspan=2, sticky="nsew")
frameC.grid_propagate(False)

label3 = tk.Label(frameC, text="Frame C")
label3.pack()

#Hacer que las columnas y filas crezcan proporcialmente
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(1, weight=1)

ventana.mainloop()