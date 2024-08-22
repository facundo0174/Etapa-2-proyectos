'''
COSAS A PARCHEAR/FIXEAR/ARREGLAR/TENER EN CUENTA
-control de formato en la fecha (solo si es posible)
-control de entrada, si o si deben estar llenos los campos o seleccionados las opciones.

-configuracion de mensajes de errores en acciones no autorizadas u acotadas
'''
import tkinter
from tkinter import ttk

ventana_prueba=tkinter.Tk()
ventana_prueba.geometry("500x500")
ventana_prueba.grid_columnconfigure(0,weight=1)
ventana_prueba.grid_columnconfigure(1,weight=1)
ventana_prueba.grid_columnconfigure(2,weight=1)
ventana_prueba.grid_columnconfigure(3,weight=1)

lista_pedidos=[]
pagina_actual=0
maximo_por_pagina=10

class pedidos:
    def __init__(self):
        self.material=tkinter.StringVar(value="acrilico") #hay distintos tipos, pero debe ser acotado, acrilico/MDF(madera)/polifan/vinilo/otros varios
        self.cantidad=tkinter.StringVar() #se dvide en cuadrantes, cada plancha de 50x50 tiene 4
        self.descripcion=tkinter.StringVar() #info creativa
        self.fecha_entrega=tkinter.StringVar() #si o si formato dd/mm/aaaa y convertilo en str
        self.importe=tkinter.StringVar() #estimado facturado? confirmalo a futuro
        self.adelanto=tkinter.StringVar()
        self.estado=tkinter.StringVar(value="Iniciado") # creeria que deberia ser {/iniciado/en proceso/finalizado/retirado}, confirmar a futuro

    def alta(self):
        #creacion de ventana emergente
        ventana_registro=tkinter.Toplevel()
        ventana_registro.title("Registro De Pedido.")
        ventana_registro.geometry("500x500")
        #titulo material
        tkinter.Label(ventana_registro,text="Tipo de material: ").grid(row=0,column=0,pady=15)
        #desplegable de material
        lista_materiales=["acrilico","MDF(madera)","polifan","otros/varios"]
        desplegable_material=tkinter.OptionMenu(ventana_registro,self.material,*lista_materiales)
        desplegable_material.grid(row=0,column=1,pady=15)
        #titulos y variables para inicializar el objeto
        label_cantidad=tkinter.Label(ventana_registro,text="Ingrese la cantidad: ")
        label_importe=tkinter.Label(ventana_registro,text="Ingrese el importe total: ")
        label_adelanto=tkinter.Label(ventana_registro,text="Ingrese el adelanto total: ")
        cantidad_entry=tkinter.Entry(ventana_registro,textvariable=self.cantidad,width="40")
        importe_entry=tkinter.Entry(ventana_registro,textvariable=self.importe,width="40")
        adelanto_entry=tkinter.Entry(ventana_registro,textvariable=self.adelanto,width="40")
        label_fecha=tkinter.Label(ventana_registro,text="Fecha De Entrega (DD/MM/AAAA): ")
        fecha_entry=tkinter.Entry(ventana_registro,textvariable=self.fecha_entrega,width="40")
        label_cantidad.grid(row=1,column=0,pady=15)
        cantidad_entry.grid(row=1,column=1,pady=15)
        label_importe.grid(row=2,column=0,pady=15)
        importe_entry.grid(row=2,column=1,pady=15)
        label_adelanto.grid(row=3,column=0,pady=15)
        adelanto_entry.grid(row=3,column=1,pady=15)
        label_fecha.grid(row=4,column=0,pady=15)
        fecha_entry.grid(row=4,column=1,pady=15)
        #titulo estado
        tkinter.Label(ventana_registro,text="Estado actual: ").grid(row=5,column=0)
        #desplegable de estado
        lista_estado=["Iniciado","En Proceso","Finalizado","Retirado"]
        desplegable_estado=tkinter.OptionMenu(ventana_registro,self.estado,*lista_estado)
        desplegable_estado.grid(row=5,column=1)
        #label descripcion
        label_descripcion=tkinter.Label(ventana_registro,text="Descripcion del proyecto: ")
        descripcion_entry=tkinter.Entry(ventana_registro,textvariable=self.descripcion,width="40")
        label_descripcion.grid(row=6,column=0,pady=15)
        descripcion_entry.grid(row=7,column=1,columnspan=4,pady=15)

        tkinter.Button(ventana_registro,text="Nuevo pedido.",height=5,width=15,command= lambda:self.confirmar_datos(ventana_registro,cantidad_entry,descripcion_entry,importe_entry,adelanto_entry,fecha_entry)).grid(row=8,column=1,columnspan=4,pady=15)

    def confirmar_datos(self,ventana_registro,cantidad_entry,descripcion_entry,importe_entry,adelanto_entry,fecha_entry):
        #modificacion de variable de instancia actual --TODAS-- y agregacion de nuevo objeto a la lista.
        cantidad_entry=cantidad_entry
        descripcion_entry=descripcion_entry
        importe_entry=importe_entry
        adelanto_entry=adelanto_entry
        fecha_entry=fecha_entry
        setter_cantidad=str(cantidad_entry.get())
        setter_descripcion=str(descripcion_entry.get())
        setter_importe=str(importe_entry.get())
        setter_adelanto=str(adelanto_entry.get())
        setter_fecha=str(fecha_entry.get())
        nuevo_pedido=pedidos()
        nuevo_pedido.cantidad.set(setter_cantidad)
        nuevo_pedido.descripcion.set(setter_descripcion)
        nuevo_pedido.importe.set(setter_importe)
        nuevo_pedido.adelanto.set(setter_adelanto)
        nuevo_pedido.fecha_entrega.set(setter_fecha)
        lista_pedidos.append(nuevo_pedido)
        ventana_registro.destroy()
    
    def __str__(self):
        return(f"(#) cantidad: {self.cantidad}, Importe: {self.importe}, Adelanto: {self.adelanto}, Estado: {self.estado}, Fecha de entrega: {self.fecha_entrega}")

    def listar(self):
        ventana_lista=tkinter.Toplevel()
        ventana_lista.title("LISTADO DE PEDIDOS")
        self.frame_pedido=tkinter.Frame(ventana_lista)
        self.frame_pedido.pack(pady=20)
        anterior=ttk.Button(ventana_lista,text="ANTERIOR",command='''self.pagina_anterior''')
        anterior.pack(side=tkinter.LEFT, padx=10)
        siguiente=ttk.Button(ventana_lista,text="SIGUIENTE",command='''self.pagina_siguiente''')
        siguiente.pack(side=tkinter.RIGHT, padx=10)
        self.mostrar()

    def mostrar(self):
        global pagina_actual
        global maximo_por_pagina
        global lista_pedidos
        for widget in self.frame.winfo_children():
            widget.destroy()

        inicio= pagina_actual * maximo_por_pagina
        fin = inicio + maximo_por_pagina
        pedido_mostrado=lista_pedidos[inicio:fin]
        for i, pedido in enumerate(pedido_mostrado):
            etiqueta_pedido = tkinter.Label(self.frame_pedidos, text=str(pedido), wraplength=400, justify=tkinter.LEFT)
            etiqueta_pedido.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            boton_descripcion = ttk.Button(self.frame_pedidos, text="Mostrar Descripción", command=lambda p=pedido: self.mostrar_descripcion(p))
            boton_descripcion.grid(row=i, column=1, padx=5, pady=5)
            ##mirar aca para meter luego acciones
        anterior.config(state=tkinter.NORMAL if self.pagina_actual > 0 else tkinter.DISABLED)
        siguiente.config(state=tkinter.NORMAL if fin < len(lista_pedidos) else tkinter.DISABLED)

    def pagina_anterior(self):
        if self.pagina_actual > 0:
            self.pagina_actual -= 1
            self.mostrar_pagina()

    def pagina_siguiente(self):
        if (self.pagina_actual + 1) * self.pedidos_por_pagina < len(lista_pedidos):
            self.pagina_actual += 1
            self.mostrar_pagina()


    def mostrar_pagina(self,anterior,siguiente,frame_pedido):
        
        inicio= pagina_actual * maximo_por_pagina
        fin = inicio + maximo_por_pagina
        pedido_mostrado=lista_pedidos[inicio:fin]
        for i, pedido in enumerate(pedidos_a_mostrar):
            etiqueta_pedido = tkinter.Label(self.frame_pedidos, text=str(pedido), wraplength=400, justify=tkinter.LEFT)
            etiqueta_pedido.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            boton_descripcion = ttk.Button(self.frame_pedidos, text="Mostrar Descripción", command=lambda p=pedido: self.mostrar_descripcion(p))
            boton_descripcion.grid(row=i, column=1, padx=5, pady=5)
            ##mirar aca para meter luego acciones
        anterior.config(state=tkinter.NORMAL if self.pagina_actual > 0 else tkinter.DISABLED)
        siguiente.config(state=tkinter.NORMAL if fin < len(lista_pedidos) else tkinter.DISABLED)

        


        pass

pedido=pedidos()
'''creacion de un objeto plantilla para acceder a metodos y crear a partir de el otros, a su ves este se REESCRIBE
para la inicializacion de otro objeto, basicamente es una variable/objeto base/ventana/plantilla'''



tkinter.Button(text="Alta",command=pedido.alta).grid(row=0,column=0)
tkinter.Button(text="listar pedidos",command='''listar''').grid(row=0,column=1)

#tkinter.Button(text="baja",command='''quitar''').grid(row=1,column=2)
#tkinter.Button(text="modificar",command='''modificar''').grid(row=2,column=2)
'''
def agregar():
'''



ventana_prueba.mainloop()