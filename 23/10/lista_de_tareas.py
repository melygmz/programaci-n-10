import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, f"✔️ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Tareas Pendientes")

# Crear el marco superior para la entrada y el botón de agregar
frame_superior = tk.Frame(ventana)
frame_superior.pack(pady=10)

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(frame_superior, width=40)
entrada_tarea.pack(side=tk.LEFT, padx=10)

# Botón para agregar tareas
boton_agregar = tk.Button(frame_superior, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT)

# Lista donde se mostrarán las tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

# Crear el marco inferior para los botones de acción
frame_inferior = tk.Frame(ventana)
frame_inferior.pack(pady=10)

# Botón para marcar tareas como completadas
boton_completar = tk.Button(frame_inferior, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(side=tk.LEFT, padx=10)

# Botón para eliminar tareas
boton_eliminar = tk.Button(frame_inferior, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(side=tk.LEFT, padx=10)

# Ejecutar la aplicación
ventana.mainloop()
