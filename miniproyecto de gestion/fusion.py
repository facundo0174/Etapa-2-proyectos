import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import schedule
from tkcalendar import DateEntry
import time


class pedidos:
    def __init__(self, ventanaMain, lista):
        self.ventanaMain = ventanaMain
        self.lista = lista
        self.cliente = tk.StringVar()
        self.material = tk.StringVar(value="acrilico")
        self.cantidad = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.fecha_entrega = tk.StringVar()
        self.importe = tk.StringVar()
        self.adelanto = tk.StringVar()
        self.estado = tk.StringVar(value="Iniciado")

    def alta(self):
        ventanaAlta = tk.Toplevel()
        ventanaAlta.title("REGISTRO DE PEDIDO")
        ventanaAlta.geometry("500x600")
        
        #ingresar la información
        tk.Label(ventanaAlta, text="Nombre y Apellido:").grid(row=0, column=0, pady=15)
        cliente_entry = tk.Entry(ventanaAlta, textvariable=self.cliente, width=40)
        cliente_entry.grid(row=0, column=1, pady=15)

        tk.Label(ventanaAlta, text="Tipo de material:").grid(row=1, column=0, pady=15)
        lista_materiales = ["acrilico", "MDF(madera)", "polifan", "otros/varios"]
        desplegable_material = tk.OptionMenu(ventanaAlta, self.material, *lista_materiales)
        desplegable_material.grid(row=1, column=1, pady=15)

        tk.Label(ventanaAlta, text="Cantidad:").grid(row=2, column=0, pady=15)
        cantidad_entry = tk.Entry(ventanaAlta, textvariable=self.cantidad, width=40)
        cantidad_entry.grid(row=2, column=1, pady=15)

        tk.Label(ventanaAlta, text="Importe total:").grid(row=3, column=0, pady=15)
        importe_entry = tk.Entry(ventanaAlta, textvariable=self.importe, width=40)
        importe_entry.grid(row=3, column=1, pady=15)

        tk.Label(ventanaAlta, text="Adelanto total:").grid(row=4, column=0, pady=15)
        adelanto_entry = tk.Entry(ventanaAlta, textvariable=self.adelanto, width=40)
        adelanto_entry.grid(row=4, column=1, pady=15)

        tk.Label(ventanaAlta, text="Fecha de entrega (DD/MM/AAAA):").grid(row=5, column=0, pady=15)
        fecha_entry = DateEntry(ventanaAlta, textvariable=self.fecha_entrega, width=40, date_pattern='dd/mm/yyyy')
        fecha_entry.grid(row=5, column=1, pady=15)

        tk.Label(ventanaAlta, text="Descripcion del proyecto:").grid(row=6, column=0, pady=15)
        descripcion_entry = tk.Entry(ventanaAlta, textvariable=self.descripcion, width=40)
        descripcion_entry.grid(row=6, column=1, pady=15)

        tk.Label(ventanaAlta, text="Estado actual:").grid(row=7, column=0, pady=15)
        lista_estado = ["Iniciado", "En Proceso", "Finalizado", "Retirado"]
        desplegable_estado = tk.OptionMenu(ventanaAlta, self.estado, *lista_estado)
        desplegable_estado.grid(row=7, column=1, pady=15)

        tk.Button(ventanaAlta, text="Guardar pedido", height=2, width=20, command=lambda: self.confirmar_datos(ventanaAlta)).grid(row=8, column=1, pady=15)

    def confirmar_datos(self, ventanaAlta):
        #crear un nuevo pedido
        nuevo_pedido = pedidos(self.ventanaMain, self.lista)
        nuevo_pedido.cliente.set(self.cliente.get().upper())
        nuevo_pedido.cantidad.set(self.cantidad.get())
        nuevo_pedido.importe.set(self.importe.get())
        nuevo_pedido.adelanto.set(self.adelanto.get())
        nuevo_pedido.fecha_entrega.set(self.fecha_entrega.get())
        nuevo_pedido.material.set(self.material.get().upper())
        nuevo_pedido.estado.set(self.estado.get().upper())
        nuevo_pedido.descripcion.set(self.descripcion.get().upper())

        #agregar pedido a la lista
        self.lista.append(nuevo_pedido)

        #programar alarma
        self.programar_alarma(nuevo_pedido)
        
        #cerrar ventana de alta
        ventanaAlta.destroy()

    def programar_alarma(self, pedido):
        fecha_entrega = datetime.datetime.strptime(pedido.fecha_entrega.get(), '%d/%m/%Y')
        fecha_alarma = fecha_entrega - datetime.timedelta(days=7)
        print(f"Alarma programada para el {fecha_alarma.strftime('%Y-%m-%d')} del pedido '{pedido.descripcion.get()}'")
        schedule.every().day.at("00:00").do(self.generar_alarma, pedido=pedido)

    def generar_alarma(self, pedido):
        messagebox.showinfo(f"El pedido '{pedido.descripcion.get()}' se entrega en 7 días. Fecha de entrega: {pedido.fecha_entrega.get()}")

    def modificar(self, pedido):
        ventanaModificar = tk.Toplevel()
        ventanaModificar.title("Modificar Pedido")
        ventanaModificar.geometry("500x600")
        
        #mostrar lista pedidos y poder modificar
        tk.Label(ventanaModificar, text="Modificar cantidad:").grid(row=0, column=0, pady=15)
        cantidad_entry = tk.Entry(ventanaModificar, textvariable=pedido.cantidad, width=40)
        cantidad_entry.grid(row=0, column=1, pady=15)

        tk.Label(ventanaModificar, text="Modificar descripcion:").grid(row=1, column=0, pady=15)
        descripcion_entry = tk.Entry(ventanaModificar, textvariable=pedido.descripcion, width=40)
        descripcion_entry.grid(row=1, column=1, pady=15)

        tk.Label(ventanaModificar, text="Modificar importe:").grid(row=2, column=0, pady=15)
        importe_entry = tk.Entry(ventanaModificar, textvariable=pedido.importe, width=40)
        importe_entry.grid(row=2, column=1, pady=15)

        tk.Label(ventanaModificar, text="Modificar adelanto:").grid(row=3, column=0, pady=15)
        adelanto_entry = tk.Entry(ventanaModificar, textvariable=pedido.adelanto, width=40)
        adelanto_entry.grid(row=3, column=1, pady=15)

        tk.Label(ventanaModificar, text="Modificar fecha de entrega (DD/MM/AAAA):").grid(row=4, column=0, pady=15)
        fecha_entry = DateEntry(ventanaModificar, textvariable=pedido.fecha_entrega, width=40, date_pattern='dd/mm/yyyy')
        fecha_entry.grid(row=4, column=1, pady=15)

        tk.Button(ventanaModificar, text="Guardar cambios", height=2, width=20, command=lambda: self.guardar_cambios(ventanaModificar, pedido)).grid(row=5, column=1, pady=15)

    def guardar_cambios(self, ventanaModificar, pedido):
        #cambiar alarma de pedido modif
        self.programar_alarma(pedido)
        ventanaModificar.destroy()

    def __str__(self):
        return f"Cliente: {self.cliente.get()}, Material: {self.material.get()}, Cantidad: {self.cantidad.get()}, Importe: {self.importe.get()}, Adelanto: {self.adelanto.get()}, Fecha entrega: {self.fecha_entrega.get()}, Estado: {self.estado.get()}"


class main:
    def __init__(self):
        self.lista_pedidos = []
        self.ventanaPrueba = tk.Tk()
        obj_pedido = pedidos(self.ventanaPrueba, self.lista_pedidos)
        self.ventanaPrueba.title("Gestion de Pedidos")
        self.ventanaPrueba.geometry("500x500")
        
        #botones menu
        tk.Button(self.ventanaPrueba, text="Alta Pedido", command=obj_pedido.alta).pack(pady=10)
        tk.Button(self.ventanaPrueba, text="Lista Pedidos", command=self.listar).pack(pady=10)
        tk.Button(self.ventanaPrueba, text="Modificar Pedido", command=self.modificar_pedido).pack(pady=10)

    def listar(self):
        ventanaListar = tk.Toplevel()
        ventanaListar.title("Lista de Pedidos")
        ventanaListar.geometry("500x600")
        
        if not self.lista_pedidos:
            messagebox.showinfo("No hay pedidos registrados.")
            return

        #ver lista de pedidos
        for i, pedido in enumerate(self.lista_pedidos):
            tk.Label(ventanaListar, text=f"{i+1}. {pedido}").pack(pady=5)

    def modificar_pedido(self):
        if not self.lista_pedidos:
            messagebox.showinfo("No hay pedidos para modificar.")
            return

        #modificar pedido
        ventanaSeleccionar = tk.Toplevel()
        ventanaSeleccionar.title("Seleccionar Pedido")
        ventanaSeleccionar.geometry("300x400")

        tk.Label(ventanaSeleccionar, text="Seleccione el numero del pedido:").pack(pady=10)

        #ComboBox para elegir el pedido
        pedidos_numeros = [f"{i+1}. {pedido.cliente.get()}" for i, pedido in enumerate(self.lista_pedidos)]
        seleccionado = tk.StringVar(value=pedidos_numeros[0])
        combo = ttk.Combobox(ventanaSeleccionar, textvariable=seleccionado, values=pedidos_numeros, state="readonly")
        combo.pack(pady=10)

        def modificar_seleccionado():
            indice = int(seleccionado.get().split(".")[0]) - 1
            self.lista_pedidos[indice].modificar(self.lista_pedidos[indice])
            ventanaSeleccionar.destroy()

        tk.Button(ventanaSeleccionar, text="Modificar", command=modificar_seleccionado).pack(pady=10)



ventana = main()
ventana.ventanaPrueba.mainloop()

#hilo para las alarmas
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

import threading
threading.Thread(target=run_schedule, daemon=True).start()