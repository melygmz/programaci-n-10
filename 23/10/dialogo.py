import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        root.destroy()

root = tk.Tk()        

root.protocol("WM_DELETE_WINDOW", on_closing) # Asegurar que el cuadro de diálogo aparezca al cerrar

root.mainloop()