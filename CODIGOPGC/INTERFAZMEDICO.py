import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# Archivo donde se almacenan los pacientes
archivo_pacientes = "registro_pacientes.csv"

# Archivo para registrar la evolución de los pacientes
archivo_evolucion = "evolucion_pacientes.csv"

# Función para cargar los pacientes registrados
def cargar_pacientes():
    if not os.path.exists(archivo_pacientes):
        messagebox.showwarning("Advertencia", "No hay pacientes registrados aún.")
        return
    
    tree.delete(*tree.get_children())  # Limpiar la tabla antes de recargar datos

    with open(archivo_pacientes, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila (encabezado)
        for row in reader:
            tree.insert("", tk.END, values=row)

# Función para registrar la evolución del paciente
def registrar_evolucion():
    seleccionado = tree.selection()
    
    if not seleccionado:
        messagebox.showerror("Error", "Seleccione un paciente para actualizar su evolución.")
        return
    
    paciente = tree.item(seleccionado, "values")
    nombre, edad, genero, sintomas, urgencia = paciente

    evolucion = entry_evolucion.get("1.0", tk.END).strip()
    
    if not evolucion:
        messagebox.showerror("Error", "Debe ingresar una evolución o procedimiento realizado.")
        return

    # Guardar la evolución en el archivo
    archivo_existe = os.path.exists(archivo_evolucion)

    with open(archivo_evolucion, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not archivo_existe:
            writer.writerow(["Nombre", "Edad", "Género", "Síntomas", "Nivel de Urgencia", "Evolución"])
        writer.writerow([nombre, edad, genero, sintomas, urgencia, evolucion])
    
    messagebox.showinfo("Éxito", f"Evolución de {nombre} registrada correctamente.")
    entry_evolucion.delete("1.0", tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Control de Pacientes - Personal Médico")
root.geometry("700x500")
root.resizable(False, False)

# Etiqueta título
tk.Label(root, text="Lista de Pacientes Registrados", font=("Arial", 14, "bold")).pack(pady=10)

# Tabla de pacientes
frame = tk.Frame(root)
frame.pack()

columns = ("Nombre", "Edad", "Género", "Síntomas", "Nivel de Urgencia")
tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack()

# Botón para cargar pacientes
boton_cargar = tk.Button(root, text="Cargar Pacientes", font=("Arial", 10, "bold"), bg="blue", fg="white", command=cargar_pacientes)
boton_cargar.pack(pady=5)

# Sección de evolución médica
tk.Label(root, text="Registrar Evolución / Procedimiento", font=("Arial", 12, "bold")).pack(pady=10)
entry_evolucion = tk.Text(root, width=80, height=4)
entry_evolucion.pack()

# Botón para registrar evolución
boton_registrar = tk.Button(root, text="Registrar Evolución", font=("Arial", 10, "bold"), bg="green", fg="white", command=registrar_evolucion)
boton_registrar.pack(pady=5)

# Botón para salir
boton_salir = tk.Button(root, text="Salir", font=("Arial", 10), bg="red", fg="white", command=root.quit)
boton_salir.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
