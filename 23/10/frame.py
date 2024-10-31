import tkinter as tk

root = tk.Tk()

# Crear un frame para los botones de numéricos
frame_numeros = tk.Frame(root)
frame_numeros.pack(side=tk.LEFT)

# Crear un frame para los botones de operaciones
frame_operaciones = tk.Frame(root)
frame_operaciones.pack(side=tk.RIGHT)

# Agregar botones a los frames
for i in range(9):
    button = tk.Button(frame_numeros, text=str(i+1), width=5, height=2)
    button.pack(side=tk.TOP)

button_plus = tk.Button(frame_operaciones, text="+", width=5, height=2)
button_plus.pack(side=tk.TOP)

root.mainloop()