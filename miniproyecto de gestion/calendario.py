#instalar 'pip install tkcalendar' y  'pip install schedule' en una terminal nueva para que funcione el codigo
import datetime
import schedule
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry

# Lista de pedidos
pedidos = []

# Funcion para generar alarma
def generar_alarma(pedido):
    messagebox.showinfo("Alerta!!", f" El pedido '{pedido['descripcion']}' tiene su entrega en 7 días. Fecha de entrega: {pedido['fecha_entrega']}")

# Funcion programar alarma
def programar_alarma(pedido):
    # menos 7 días a la fecha de entrega
    fecha_alarma = pedido['fecha_entrega'] - datetime.timedelta(days=7)
    print(f"Alarma programada para el {fecha_alarma.strftime('%Y-%m-%d')} del pedido '{pedido['descripcion']}'")
    # Programar alarma a las 00:00
    schedule.every().day.at("00:00").do(generar_alarma, pedido=pedido)

# funcion para convertir cadena de texto en objeto datetime
def convertir_fecha(fecha_str):
    return datetime.datetime.strptime(fecha_str, '%Y-%m-%d')

# se agrega informacion para pedido
def agregar_pedido():
    nombre_cliente = nombre_entry.get()
    apellido_cliente = apellido_entry.get()
    descripcion = descripcion_entry.get()
    fecha_entrega_str = fecha_entrega_entry.get_date().strftime('%Y-%m-%d')

    # Convertir la fecha de entrega de string a datetime
    fecha_entrega = convertir_fecha(fecha_entrega_str)

    # pedido
    pedido = {
        'nombre_cliente': nombre_cliente,
        'apellido_cliente': apellido_cliente,
        'fecha_pedido': datetime.datetime.today(),
        'descripcion': descripcion,
        'fecha_entrega': fecha_entrega
    }

    # Agregar a la lista de pedidos
    pedidos.append(pedido)
    
    # Programar alarma
    programar_alarma(pedido)
    messagebox.showinfo(f"Pedido agregado con exito!. Alarma programada para el {fecha_entrega.strftime('%Y-%m-%d')}")

# Funcion para mostrar y modificar pedidos
def ver_pedidos():
    if not pedidos:
        messagebox.showinfo("Lista de Pedidos", "No hay pedidos.")
        return

    pedidos_texto = ""
    for i, pedido in enumerate(pedidos):
        pedidos_texto += (f"Pedido {i+1}:\n"
                          f"Nombre: {pedido['nombre_cliente']} {pedido['apellido_cliente']}\n"
                          f"Descripción: {pedido['descripcion']}\n"
                          f"Fecha de Pedido: {pedido['fecha_pedido'].strftime('%Y-%m-%d')}\n"
                          f"Fecha de Entrega: {pedido['fecha_entrega'].strftime('%Y-%m-%d')}\n\n")

    # Mostrar los pedidos ventana aparte
    mensaje = tk.Toplevel(ventana)
    mensaje.title("Lista de Pedidos")
    tk.Label(mensaje, text="Pedidos:\n\n" + pedidos_texto).pack(padx=10, pady=10)
    
    # Boton (modificar un pedido)
    modificar_btn = tk.Button(mensaje, text="Modificar Pedido", command=lambda: modificar_pedido(mensaje))
    modificar_btn.pack(pady=10)

# Modificar pedido
def modificar_pedido(mensaje):
    # número del pedido para modificar
    numero_pedido = simpledialog.askinteger("Modificar Pedido", "Ingrese el número del pedido que desea modificar:")
    if numero_pedido is None or numero_pedido <= 0 or numero_pedido > len(pedidos):
        messagebox.showerror("Error!!", "Numero de pedido no existe.")
        return

    pedido = pedidos[numero_pedido - 1]
    
    # Informacion del pedido
    nombre_cliente = simpledialog.askstring("Modificar Pedido", f"Ingrese el nuevo nombre del cliente (actual: {pedido['nombre_cliente']}):", initialvalue=pedido['nombre_cliente'])
    apellido_cliente = simpledialog.askstring("Modificar Pedido", f"Ingrese el nuevo apellido del cliente (actual: {pedido['apellido_cliente']}):", initialvalue=pedido['apellido_cliente'])
    descripcion = simpledialog.askstring("Modificar Pedido", f"Ingrese la nueva descripción del pedido (actual: {pedido['descripcion']}):", initialvalue=pedido['descripcion'])
    fecha_entrega_str = simpledialog.askstring("Modificar Pedido", f"Ingrese la nueva fecha de entrega (actual: {pedido['fecha_entrega'].strftime('%Y-%m-%d')}):", initialvalue=pedido['fecha_entrega'].strftime('%Y-%m-%d'))
    
    if nombre_cliente and apellido_cliente and descripcion and fecha_entrega_str:
        fecha_entrega = convertir_fecha(fecha_entrega_str)
        pedidos[numero_pedido - 1] = {
            'nombre_cliente': nombre_cliente,
            'apellido_cliente': apellido_cliente,
            'fecha_pedido': datetime.datetime.today(),
            'descripcion': descripcion,
            'fecha_entrega': fecha_entrega
        }
        # Actualizar la alarma
        programar_alarma(pedidos[numero_pedido - 1])
        messagebox.showinfo("Pedido modificado con exito!")
        mensaje.destroy()

# Ventana
ventana = tk.Tk()
ventana.title("Gestion de Pedidos")

# Entrada de datos (Nombre - Apellido - Descripcion - Fecha)
tk.Label(ventana, text="Nombre del cliente:").grid(row=0, column=0, padx=10, pady=10)
nombre_entry = tk.Entry(ventana, width=50)
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Apellido del cliente:").grid(row=1, column=0, padx=10, pady=10)
apellido_entry = tk.Entry(ventana, width=50)
apellido_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Descripcion del pedido:").grid(row=2, column=0, padx=10, pady=10)
descripcion_entry = tk.Entry(ventana, width=50)
descripcion_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Fecha de entrega (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=10)
fecha_entrega_entry = DateEntry(ventana, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
fecha_entrega_entry.grid(row=3, column=1, padx=10, pady=10)

# Botones 'agregar pedido' y 'ver pedidos'
agregar_pedido_btn = tk.Button(ventana, text="Agregar Pedido", command=agregar_pedido)
agregar_pedido_btn.grid(row=4, column=1, padx=10, pady=10)

ver_pedidos_btn = tk.Button(ventana, text="Ver Pedidos", command=ver_pedidos)
ver_pedidos_btn.grid(row=5, column=1, padx=10, pady=10)

# bucle para mantener la ventana abierta
def mantener_programa():
    while True:
        schedule.run_pending()
        time.sleep(1)

# hilo para ejecutar el bucle de programación de alarmas
import threading
hilo = threading.Thread(target=mantener_programa, daemon=True)
hilo.start()

ventana.mainloop()
