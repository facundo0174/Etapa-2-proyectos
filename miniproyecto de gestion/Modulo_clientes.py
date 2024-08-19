import tkinter
from tkinter import ttk

ventana_prueba=tkinter.Tk()
ventana_prueba.geometry("500x500")


lista_pedidos=[]


class pedidos:
    def __init__(self):
        self.material=tkinter.StringVar() #hay distintos tipos, pero debe ser acotado, acrilico/MDF(madera)/polifan/vinilo/otros varios
        self.cantidad=tkinter.StringVar() #se dvide en cuadrantes, cada plancha de 50x50 tiene 4
        self.descripcion=tkinter.StringVar() #info creativa
        self.fecha_entrega=tkinter.StringVar() #si o si formato dd/mm/aaaa y convertilo en str
        self.importe=tkinter.StringVar() #estimado facturado? confirmalo a futuro
        self.adelanto=tkinter.StringVar()
        self.estado=tkinter.StringVar() # creeria que deberia ser {/iniciado/en proceso/finalizado/retirado}, confirmar a futuro

    def alta(self):
        #creacion de ventana emergente
        ventana_registro=tkinter.Toplevel()
        ventana_registro.title("Registro De Pedido.")
        ventana_registro.geometry("500x500")
        #titulo material
        tkinter.Label(ventana_registro,text="Tipo de material: ").grid(row=0,column=0,pady=15)
        #desplegable de material
        lista_materiales=["acrilico","MDF(madera)","polifan","otros/varios"]
        desplegable_material=tkinter.OptionMenu(ventana_registro,self.material,lista_materiales[0],*lista_materiales)
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
        desplegable_estado=tkinter.OptionMenu(ventana_registro,self.estado,lista_estado[0],*lista_estado)
        desplegable_estado.grid(row=5,column=1)
        #label descripcion
        label_descripcion=tkinter.Label(ventana_registro,text="Descripcion del proyecto: ")
        descripcion_entry=tkinter.Entry(ventana_registro,textvariable=self.descripcion,width="40")
        label_descripcion.grid(row=6,column=0,pady=15)
        descripcion_entry.grid(row=7,column=1,columnspan=4,pady=15)

        tkinter.Button(ventana_registro,text="Validar",height=5,width=15,command=self.confirmar_datos).grid(row=8,column=1,columnspan=4,pady=15)

    def confirmar_datos(self):
        #modificacion de variable de instancia actual --TODAS--.
        setter_cantidad=str(self.cantidad_entry.get())
        setter_descripcion=self.descripcion_entry.get()
        setter_importe=str(self.importe_entry.get())
        setter_adelanto=str(self.adelanto.get())
        setter_fecha=str(self.fecha_entry.get())
        self.cantidad.set(setter_cantidad)
        self.descripcion.set(setter_descripcion)
        self.importe.set(setter_importe)
        self.adelanto.set(setter_adelanto)
        self.fecha_entrega.set(setter_fecha)
        


        

pedido=pedidos()


tkinter.Button(text="Alta",command=pedido.alta).grid(row=0,column=2)
tkinter.Button(text="baja",command='''quitar''').grid(row=1,column=2)
tkinter.Button(text="modificar",command='''modificar''').grid(row=2,column=2)
'''
def agregar():
'''



ventana_prueba.mainloop()