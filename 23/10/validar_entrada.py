import tkinter as tk
from tkinter import messagebox

def validar():
    entrada = entry.get()
    if entrada.isdigit():
        messagebox.showinfo("Validación", "Entrada válida")

root = tk.Tk()        

entry = tk.Entry(root)
entry.pack()

boton_validar = tk.Button(root, text="Validar", command=validar)
boton_validar.pack()

root.mainloop()