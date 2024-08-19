import tkinter as tk

# Función para mostrar la opción seleccionada
def mostrar_seleccion():
    seleccion = variable.get()
    print(f"Opción seleccionada: {seleccion}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Desplegable")

# Crear una variable para almacenar la opción seleccionada
variable = tk.StringVar(ventana)
variable.set("Opción 1")  # Valor predeterminado

# Crear el menú desplegable
opciones = ["Opción 1", "Opción 2", "Opción 3"]
menu_desplegable = tk.OptionMenu(ventana, variable, *opciones)
menu_desplegable.pack(pady=10)

# Crear un botón para mostrar la opción seleccionada
boton = tk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
boton.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
