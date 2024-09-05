'''
COSAS A PARCHEAR/FIXEAR/ARREGLAR/TENER EN CUENTA
-control de formato en la fecha (solo si es posible)
-control de entrada, si o si deben estar llenos los campos o seleccionados las opciones.
-modulo de BAJAS
-modulo de Modificaciones
_integracion con un boton "ACCION" que muestre las 2 posibilidades anteriores.
-configuracion de mensajes de errores en acciones no autorizadas u acotadas
- opcion de aplicar UNICODE para quitar acentos y parametrizar un estandar sobre la entrada de texto manejada
'''
import tkinter as tk
from tkinter import ttk

class pedidos:
    def __init__(self,ventanaMain,lista):
        self.ventanaMain=ventanaMain
        self.lista=lista
        self.cliente=tk.StringVar()
        #self.telefono
        #self.direccion 
        #confirmar a futuro
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
        ventanaAlta.geometry("500x600")
        #titulo material
        tk.Label(ventanaAlta,text="Tipo de material: ").grid(row=1,column=0,pady=15)
        #desplegable de material
        lista_materiales=["acrilico","MDF(madera)","polifan","otros/varios"]
        desplegable_material=tk.OptionMenu(ventanaAlta,self.material,*lista_materiales)
        desplegable_material.grid(row=1,column=1,pady=15)
        #titulos y variables para inicializar el objeto
        label_cantidad=tk.Label(ventanaAlta,text="Ingrese la cantidad: ")
        label_importe=tk.Label(ventanaAlta,text="Ingrese el importe total: ")
        label_adelanto=tk.Label(ventanaAlta,text="Ingrese el adelanto total: ")
        cantidad_entry=tk.Entry(ventanaAlta,textvariable=self.cantidad,width="40")
        importe_entry=tk.Entry(ventanaAlta,textvariable=self.importe,width="40")
        adelanto_entry=tk.Entry(ventanaAlta,textvariable=self.adelanto,width="40")
        label_fecha=tk.Label(ventanaAlta,text="Fecha De Entrega (DD/MM/AAAA): ")
        fecha_entry=tk.Entry(ventanaAlta,textvariable=self.fecha_entrega,width="40")
        label_cliente=tk.Label(ventanaAlta,text="Apellid y nombre")
        cliente_entry=tk.Entry(ventanaAlta,textvariable=self.cliente,width="40")
        label_cliente.grid(row=0,column=0,pady=15)
        cliente_entry.grid(row=0,column=1,pady=15)
        label_cantidad.grid(row=3,column=0,pady=15)
        cantidad_entry.grid(row=3,column=1,pady=15)
        label_importe.grid(row=4,column=0,pady=15)
        importe_entry.grid(row=4,column=1,pady=15)
        label_adelanto.grid(row=5,column=0,pady=15)
        adelanto_entry.grid(row=5,column=1,pady=15)
        label_fecha.grid(row=6,column=0,pady=15)
        fecha_entry.grid(row=6,column=1,pady=15)
        #titulo estado
        tk.Label(ventanaAlta,text="Estado actual: ").grid(row=7,column=0)
        #desplegable de estado
        lista_estado=["Iniciado","En Proceso","Finalizado","Retirado"]
        desplegable_estado=tk.OptionMenu(ventanaAlta,self.estado,*lista_estado)
        desplegable_estado.grid(row=7,column=1)
        #label descripcion
        label_descripcion=tk.Label(ventanaAlta,text="Descripcion del proyecto: ")
        descripcion_entry=tk.Entry(ventanaAlta,textvariable=self.descripcion,width="40")
        label_descripcion.grid(row=8,column=0,pady=15)
        descripcion_entry.grid(row=9,column=1,columnspan=4,pady=15)

        tk.Button(ventanaAlta,text="Nuevo pedido.",height=5,width=15,command= lambda:self.confirmar_datos(ventanaAlta,cantidad_entry,descripcion_entry,importe_entry,adelanto_entry,fecha_entry,cliente_entry)).grid(row=10,column=1,columnspan=4,pady=15)
    
    def confirmar_datos(self,ventanaAlta,cantidad_entry,descripcion_entry,importe_entry,adelanto_entry,fecha_entry,cliente_entry):
        #modificacion de variable de instancia actual --TODAS-- y agregacion de nuevo objeto a la lista.
        # se parametriza las mayusculas pero aun queda el caso de que ingresen acentos, ver modulo unicode para tratar este asunto
        setter_cantidad=cantidad_entry.get()
        setter_descripcion=descripcion_entry.get().upper()
        setter_importe=importe_entry.get()
        setter_adelanto=adelanto_entry.get()
        setter_fecha=fecha_entry.get()
        setter_material=self.material.get().upper()
        setter_estado=self.estado.get().upper()
        setter_cliente=cliente_entry.get().upper()
        nuevo_pedido=pedidos(self.ventanaMain,self.lista)
        nuevo_pedido.cantidad.set(setter_cantidad)
        nuevo_pedido.descripcion.set(setter_descripcion)
        nuevo_pedido.importe.set(setter_importe)
        nuevo_pedido.adelanto.set(setter_adelanto)
        nuevo_pedido.fecha_entrega.set(setter_fecha)
        nuevo_pedido.material.set(setter_material)
        nuevo_pedido.estado.set(setter_estado)
        nuevo_pedido.cliente.set(setter_cliente)
        self.lista.append(nuevo_pedido)
        #print(f"contenido interezante:{self.lista[0].material.get()}") linea para comprobar el correcto asignamiento de los objetos
        ventanaAlta.destroy()
    
    ''' 
    str() es una llamada/metodo especial el cual no necesita variabloObjeto.str() o un self.str(), esto lo intuye python con el argumento pasado
    es decir str(variableObjeto), siempre y cuando posea este metodo dentro de sus definiciones de clase u objeto, en este caso str() devolvera en formato
    string o cadena de texto el contenido de sus variables para mas adelante mostrarlo segun un label a modo de visualizacion por pantalla mediante tkinter
    '''
    def __str__(self):
        return(f"(#) cantidad: {self.cantidad.get()}, Importe: {self.importe.get()}, Adelanto: {self.adelanto.get()}, Estado: {self.estado.get()}, Fecha de entrega: {self.fecha_entrega.get()}")
    


class main:#clase contenedora de todos los objetos, seria algo asi como la ventana principal, hecha para poder usar avanzar y retroceder en paginacion
    
    def __init__(self):
        self.lista_pedidos=[]
        self.ventanaPrueba=tk.Tk()
        obj_pedido=pedidos(self.ventanaPrueba,self.lista_pedidos)#creado para acceder a metodos
        self.ventanaPrueba.title("ventana principal de prueba")
        self.ventanaPrueba.geometry("500x500")
        self.ventanaPrueba.grid_columnconfigure(0,weight=1)#configuracion que realmente no importa es simplemente para que las columnas no sean pequeñas
        self.ventanaPrueba.grid_columnconfigure(1,weight=1)
        self.ventanaPrueba.grid_columnconfigure(2,weight=1)
        self.ventanaPrueba.grid_columnconfigure(3,weight=1)
        #botones
        self.boton1=tk.Button(text="Alta",command=obj_pedido.alta)
        self.boton1.grid(row=0,column=0)
        self.boton2=tk.Button(text="listar pedidos",command=self.listar)
        self.boton2.grid(row=0,column=1)
        self.busqueda=False
    
    def listar(self): #metodo que crea emergentes para listar los pedidos contenidos en la lista
        self.pagina_actual=0#variables de control para la paginacion, esta debe ser siempre 0 inicialemente
        self.pagina_max=10# maximo de pedidos por pagina, puede variar

        self.listado=tk.Toplevel()#creacion de emergente
        self.listado.title("LISTADO DE PEDIDOS")
        self.framePedidos=ttk.Frame(self.listado)#frame hijo de pagina emergente listado
        self.framePedidos.pack(pady=15)
        self.botonSig=ttk.Button(self.listado,text="Siguiente",command=self.siguiente)
        self.botonSig.pack(side=tk.RIGHT,padx=10)# posicionamiento en esquinas inferiores
        self.botonAnt=ttk.Button(self.listado,text="Anterior",command=self.anterior)
        self.botonAnt.pack(side=tk.LEFT,padx=10)
        self.botonBuscar=ttk.Button(self.listado,text="Buscar",command=self.mostrar_busqueda)
        self.botonBuscar.pack(side=tk.LEFT,padx=10)
        self.normal=ttk.Button(self.listado,text="Todo",command=self.listadoNormal)
        self.normal.pack(side=tk.LEFT,padx=10)

        self.mostrarLista()
    
    def listadoNormal(self):
        self.busqueda=False
        self.pagina_actual=0
        self.pagina_max=10
        self.mostrarLista()

    def mostrarLista(self):#metodo que "actualiza" la lista  y luego copia el contenido del objeto de manera visible en un .Label
        for hijos in self.framePedidos.winfo_children(): 
            #funcion que devuelve a todo "hijo" objeto contenido dentro del Frame, y lo destruimos para actualizar visualmente los pedidos
            hijos.destroy()

        inicio=self.pagina_actual * self.pagina_max
        fin=inicio + self.pagina_max
        listadoAcotado=self.lista_pedidos[inicio:fin] #traemos 10 en 10 los objetos a listar

        for i, pedido in enumerate(listadoAcotado):
            #se usa enumerate para un control correcto sobre el recorrido de indices sobre iterables en este caso la lista, de esa forma
            #utilizamos variables "i" en este caso para recorrer los indices y abstraernos en el conocimiento de su valor para la obtencion del indice
            #la variable pedido se obtendra el valor del objeto en este caso el objeto pedido al cual podemos aceder a sus variables con self y get()
            etiqueta_pedido = tk.Label(self.framePedidos, text=str(pedido), wraplength=400, justify=tk.LEFT)
            etiqueta_pedido.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            
            boton_detalle = ttk.Button(self.framePedidos, text="Mostrar Descripción", command=lambda p=pedido: self.mostrar_descripcion(p))
            boton_detalle.grid(row=i, column=1, padx=5, pady=5)
        ''' el .config sirve para cambiar el estado de los botones o widget asociado, en este caso queremos "desabilitar" el boton si no existe mas paginas
        para recorrer, lo cual tiene sentido'''
        self.botonAnt.config(state=tk.NORMAL if self.pagina_actual > 0 else tk.DISABLED)
        self.botonSig.config(state=tk.NORMAL if fin < len(self.lista_pedidos) else tk.DISABLED)
    
    def mostrar_busqueda(self):
        #debo hace que elimine y con la obtencion de un entry realizar la busqueda segun la variable a encontrar dentro del objeto, si coincide la escribis.
        self.busqueda=tk.Toplevel()
        self.label_busqueda=tk.Label(self.busqueda,text="Nombre y apellido:")
        self.entry_busqueda=tk.Entry(self.busqueda)
        self.label_busqueda.pack(side="left",padx=10,pady=10)
        self.entry_busqueda.pack(side="left",padx=10,pady=10)
        self.botonBuscar=ttk.Button(self.busqueda,text="Buscar",command="buscar")
        self.botonBuscar.pack(padx=10,pady=10)
        self.busqueda=True
    
    def buscar(self):
        self.nombre_buscado= self.entry_busqueda.get().upper() #aca esta el cliente buscado
        existe=False
        self.tot_coincidencia=0
        for pedidos in self.lista_pedidos:
            if pedidos.cliente == self.nombre_buscado:
                existe=True
                self.tot_coincidencia+=1

        
        if existe:#si existe coincidencia debemos destruir todo lo mostrado en la lista y volver a recorrer la misma para escribirla discriminadamente
            self.pagina_actual=0
            self.pagina_max=10
            self.listar_busqueda()
        else:
            # se muestra busqueda fallida no existe, se setea en falso self.busqueda=False
            pass

    def listar_busqueda(self):   
        for hijos in self.framePedidos.winfo_children(): #eliminamos todo SI y SOLO SI encontro algo de antemano contrario queda como esta.
            hijos.destroy()
        
        inicio=self.pagina_actual * self.pagina_max
        fin=inicio + self.pagina_max
        listadoAcotado=self.lista_pedidos[inicio:fin] #traemos 10 en 10 los objetos a listar
        fila=0              
        for pedido in listadoAcotado:
            if pedido.cliente==self.nombre_buscado: #se le agrega que imprima solo aquellos que tengan el mismo nombre de cliente.
                etiqueta_pedido = tk.Label(self.framePedidos, text=str(pedido), wraplength=400, justify=tk.LEFT)
                etiqueta_pedido.grid(row=fila, column=0, sticky="w", padx=5, pady=5)
                boton_detalle = ttk.Button(self.framePedidos, text="Mostrar Descripción", command=lambda p=pedido: self.mostrar_descripcion(p))
                boton_detalle.grid(row=fila, column=1, padx=5, pady=5)
                ''' el .config sirve para cambiar el estado de los botones o widget asociado, en este caso queremos "desabilitar" el boton si no existe mas paginas
                para recorrer, lo cual tiene sentido'''
                fila+=1
        self.botonAnt.config(state=tk.NORMAL if self.pagina_actual > 0 else tk.DISABLED)
        self.botonSig.config(state=tk.NORMAL if fin < self.tot_coincidencia else tk.DISABLED) 
        '''anteriormente el boton siguiente se colocaba en normal si era menor a la cantidad de objetos en la lista, contrario se bloquea
        ahora si tengo 10 filas(10 objetos listados) segun la ecuacion de FIN, este no estara habilitado lo cual es logico, no puede haber pag sig
        si sucede que tengo ejemplo 15 filas(15 objetos) entonces alli si estara habilitado para realizar de nuevo el listado de los buscados
        PARA ELLO SE APLICA EL SELF.TOT_COINCIDENCIAS, para obtener el tope que obedece lo anterior'''
        pass

    def anterior(self):#actualizacion de valores de las paginas en caso de retroceder, el caso de ser no haber mas paginas a retroceder esta contemplado en .config
        if self.busqueda:
            if self.pagina_actual > 0:
                self.pagina_actual -= 1
                self.listar_busqueda() 
        else:
            if self.pagina_actual > 0:
                self.pagina_actual -= 1
                self.mostrarLista()

    def siguiente(self):
        '''actualizacion de valores de pagina asociados al boton siguiente, de nuevo solo es posible incrementar el valor/ pasar a una siguiente 
        pagina si y solo si es posible "traer" mas valores/objetos de la lista, ejemplo: no seria posible ir a la pagina 3 de una lista de longitud 13 ya que
        se muestra por pantalla de 10 en 10 pedidos a la vez, por lo cual tiene sentido el no permitir intentar "recuperar" pedidos cuando no existen 
        '''
        if self.busqueda:
            if (self.pagina_actual + 1) * self.pagina_max < self.tot_coincidencia:
                self.pagina_actual += 1
                self.listar_busqueda()
        else:
            if (self.pagina_actual + 1) * self.pagina_max < len(self.lista_pedidos):
                self.pagina_actual += 1
                self.mostrarLista()

    def mostrar_descripcion(self, pedido):
        '''
        metodo que realiza la obtencion de las descripciones de los pedidos y muestra a travez de un emergente su contenido se utiliza .text
        para formatear el texto, ya que los .entry solo dejan ingresar "lineas" de texto en otras palabras son oraciones muy largas en lugar de
        parrafos segun el caso, por lo tanto se lo utiliza para ser visualmente visualmente agradable y correcto para su lectura.
        '''
        descripcion = pedido.descripcion.get()
        #ventana emergente para mostrar la descripción
        descripcion_emergente = tk.Toplevel(self.framePedidos)
        descripcion_emergente.title("Descripción del Pedido")
        
        texto = tk.Text(descripcion_emergente, wrap=tk.WORD, width=60, height=10)
        texto.pack(pady=20)
        texto.insert(tk.END, descripcion)
        texto.config(state=tk.DISABLED)#desabilita su edicion es decir no se puede modificar el texto mostrado en pantalla

ventana=main()
ventana.ventanaPrueba.mainloop()
