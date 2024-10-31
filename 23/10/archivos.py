import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo",
                                         filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        with open(archivo, 'r') as file:
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, file.read())

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        with open(archivo, 'w') as file:
            file.write(texto.get(1.0, tk.END))

root = tk.Tk()

# Crear un campo de texto
texto = tk.Text(root, wrap="word")
texto.pack(expand=True, fill='both')

# Crear botones para abrir y guardar
boton_abrir = tk.Button(root, text="Abrir", command=abrir_archivo)
boton_abrir.pack(side=tk.LEFT)

boton_guardar = tk.Button(root, text="Guardar", command=guardar_archivo)
boton_guardar.pack(side=tk.LEFT)

root.mainloop()
