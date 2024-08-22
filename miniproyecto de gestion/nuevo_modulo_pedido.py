import tkinter as tk
from tkinter import ttk

class pedidos:
    def __init__(self,ventanaMain,lista):
        self.ventanaMain=ventanaMain
        self.lista=lista
        self.material=tk.StringVar(value="acrilico") #hay distintos tipos, pero debe ser acotado, acrilico/MDF(madera)/polifan/vinilo/otros varios
        self.cantidad=tk.StringVar() #se dvide en cuadrantes, cada plancha de 50x50 tiene 4
        self.descripcion=tk.StringVar() #info creativa
        self.fecha_entrega=tk.StringVar() #si o si formato dd/mm/aaaa y convertilo en str
        self.importe=tk.StringVar() #estimado facturado? confirmalo a futuro
        self.adelanto=tk.StringVar()
        self.estado=tk.StringVar(value="Iniciado") # creeria que deberia ser {/iniciado/en proceso/finalizado/retirado}, confirmar a futuro
        

    def alta(self):
        ventanaAlta=tk.Toplevel()
        ventanaAlta.title("REGISTRO DE PEDIDO")
        ventanaAlta.geometry("500x500")
        #titulo material
        tk.Label(ventanaAlta,text="Tipo de material: ").grid(row=0,column=0,pady=15)
        #desplegable de material
        lista_materiales=["acrilico","MDF(madera)","polifan","otros/varios"]
        desplegable_material=tk.OptionMenu(ventanaAlta,self.material,*lista_materiales)
        desplegable_material.grid(row=0,column=1,pady=15)
        #titulos y variables para inicializar el objeto
        label_cantidad=tk.Label(ventanaAlta,text="Ingrese la cantidad: ")
        label_importe=tk.Label(ventanaAlta,text="Ingrese el importe total: ")
        label_adelanto=tk.Label(ventanaAlta,text="Ingrese el adelanto total: ")
        cantidad_entry=tk.Entry(ventanaAlta,textvariable=self.cantidad,width="40")
        importe_entry=tk.Entry(ventanaAlta,textvariable=self.importe,width="40")
        adelanto_entry=tk.Entry(ventanaAlta,textvariable=self.adelanto,width="40")
        label_fecha=tk.Label(ventanaAlta,text="Fecha De Entrega (DD/MM/AAAA): ")
        fecha_entry=tk.Entry(ventanaAlta,textvariable=self.fecha_entrega,width="40")
        label_cantidad.grid(row=1,column=0,pady=15)
        cantidad_entry.grid(row=1,column=1,pady=15)
        label_importe.grid(row=2,column=0,pady=15)
        importe_entry.grid(row=2,column=1,pady=15)
        label_adelanto.grid(row=3,column=0,pady=15)
        adelanto_entry.grid(row=3,column=1,pady=15)
        label_fecha.grid(row=4,column=0,pady=15)
        fecha_entry.grid(row=4,column=1,pady=15)
        #titulo estado
        tk.Label(ventanaAlta,text="Estado actual: ").grid(row=5,column=0)
        #desplegable de estado
        lista_estado=["Iniciado","En Proceso","Finalizado","Retirado"]
        desplegable_estado=tk.OptionMenu(ventanaAlta,self.estado,*lista_estado)
        desplegable_estado.grid(row=5,column=1)
        #label descripcion
        label_descripcion=tk.Label(ventanaAlta,text="Descripcion del proyecto: ")
        descripcion_entry=tk.Entry(ventanaAlta,textvariable=self.descripcion,width="40")
        label_descripcion.grid(row=6,column=0,pady=15)
        descripcion_entry.grid(row=7,column=1,columnspan=4,pady=15)

        tk.Button(ventanaAlta,text="Nuevo pedido.",height=5,width=15,command= lambda:self.confirmar_datos(ventanaAlta,cantidad_entry,descripcion_entry,importe_entry,adelanto_entry,fecha_entry)).grid(row=8,column=1,columnspan=4,pady=15)
    
    def confirmar_datos(self,ventanaAlta,cantidad_entry,descripcion_entry,importe_entry,adelanto_entry,fecha_entry):
        #modificacion de variable de instancia actual --TODAS-- y agregacion de nuevo objeto a la lista.
        setter_cantidad=cantidad_entry.get()
        setter_descripcion=descripcion_entry.get()
        setter_importe=importe_entry.get()
        setter_adelanto=adelanto_entry.get()
        setter_fecha=fecha_entry.get()
        setter_material=self.material.get()
        setter_estado=self.estado.get()
        nuevo_pedido=pedidos(self.ventanaMain,self.lista)
        nuevo_pedido.cantidad.set(setter_cantidad)
        nuevo_pedido.descripcion.set(setter_descripcion)
        nuevo_pedido.importe.set(setter_importe)
        nuevo_pedido.adelanto.set(setter_adelanto)
        nuevo_pedido.fecha_entrega.set(setter_fecha)
        nuevo_pedido.material.set(setter_material)
        nuevo_pedido.estado.set(setter_estado)
        self.lista.append(nuevo_pedido)
        #print(f"contenido interezante:{self.lista[0].material.get()}") linea para comprobar el correcto asignamiento de los objetos
        ventanaAlta.destroy()
        


class main:
    def __init__(self):
        self.pagina_actual=0
        self.pagina_max=10
        self.lista_pedidos=[]
        self.ventanaPrueba=tk.Tk()
        obj_pedido=pedidos(self.ventanaPrueba,self.lista_pedidos)#creado para acceder a metodos
        self.ventanaPrueba.title("ventana principal de prueba")
        self.ventanaPrueba.geometry("500x500")
        self.ventanaPrueba.grid_columnconfigure(0,weight=1)#configuracion que realmente no importa
        self.ventanaPrueba.grid_columnconfigure(1,weight=1)
        self.ventanaPrueba.grid_columnconfigure(2,weight=1)
        self.ventanaPrueba.grid_columnconfigure(3,weight=1)
        #botones
        self.boton1=tk.Button(text="Alta",command=obj_pedido.alta)
        self.boton1.grid(row=0,column=0)
        self.boton2=tk.Button(text="listar pedidos",command='''listar''')
        self.boton2.grid(row=0,column=1)


ventana=main()
ventana.ventanaPrueba.mainloop()
