import tkinter as tk
from tkinter import messagebox
import csv
import os

# Función para guardar los datos del paciente en un archivo CSV
def registrar_paciente():
    nombre = entry_nombre.get().strip()
    edad = entry_edad.get().strip()
    genero = genero_var.get()
    sintomas = entry_sintomas.get("1.0", tk.END).strip()
    urgencia = urgencia_var.get()

    # Validar que todos los campos estén completos
    if not nombre or not edad.isdigit() or not sintomas or not urgencia:
        messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
        return

    # Guardar en un archivo CSV
    archivo = "registro_pacientes.csv"
    encabezado = ["Nombre", "Edad", "Género", "Síntomas", "Nivel de Urgencia"]
    datos = [nombre, edad, genero, sintomas, urgencia]

    # Verificar si el archivo existe y escribir encabezado si es necesario
    archivo_existe = os.path.exists(archivo)

    with open(archivo, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not archivo_existe:
            writer.writerow(encabezado)
        writer.writerow(datos)

    messagebox.showinfo("Éxito", f"Paciente {nombre} registrado correctamente.")
    limpiar_campos()

# Función para limpiar los campos después del registro
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_sintomas.delete("1.0", tk.END)
    genero_var.set("")
    urgencia_var.set("")

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Pacientes - Urgencias")
root.geometry("500x450")
root.resizable(False, False)

# Etiquetas y campos de entrada
tk.Label(root, text="Nombre:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nombre = tk.Entry(root, width=40)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Edad:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_edad = tk.Entry(root, width=10)
entry_edad.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Selección de Género
tk.Label(root, text="Género:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
genero_var = tk.StringVar()
tk.Radiobutton(root, text="Masculino", variable=genero_var, value="Masculino").grid(row=2, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Femenino", variable=genero_var, value="Femenino").grid(row=2, column=1, padx=110, pady=5, sticky="w")
tk.Radiobutton(root, text="Otro", variable=genero_var, value="Otro").grid(row=2, column=1, padx=200, pady=5, sticky="w")

# Campo de síntomas
tk.Label(root, text="Síntomas:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_sintomas = tk.Text(root, width=40, height=4)
entry_sintomas.grid(row=3, column=1, padx=10, pady=5)

# Selección de Nivel de Urgencia
tk.Label(root, text="Nivel de Urgencia:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
urgencia_var = tk.StringVar()
tk.Radiobutton(root, text="Leve", variable=urgencia_var, value="Leve").grid(row=4, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Moderado", variable=urgencia_var, value="Moderado").grid(row=4, column=1, padx=70, pady=5, sticky="w")
tk.Radiobutton(root, text="Crítico", variable=urgencia_var, value="Crítico").grid(row=4, column=1, padx=170, pady=5, sticky="w")

# Botón para registrar
boton_registrar = tk.Button(root, text="Registrar Paciente", font=("Arial", 12, "bold"), bg="green", fg="white", command=registrar_paciente)
boton_registrar.grid(row=5, column=0, columnspan=2, pady=20)

# Botón para salir
boton_salir = tk.Button(root, text="Salir", font=("Arial", 12), bg="red", fg="white", command=root.quit)
boton_salir.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
root.mainloop()
