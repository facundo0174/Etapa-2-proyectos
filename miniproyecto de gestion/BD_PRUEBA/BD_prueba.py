import sqlite3
import uuid #modulo de objetos permite funciones 
import datetime
import re
'''
en sqlite puedes ingresar por ejemplo cadenas de texto y estos se formatearan segun la definicion de la columna
por ejemplo tenemos un .entry que el usuario ingresa una serie de numeros, estos por la naturaleza del .entry seran 
cadenas de texto, pero sqlite al ser flexible, podemos cargar estas cadenas de texto y al pasarlas/cargarlas en la 
base de datos, estos se convertiran en numericos ya sea enteros o flotantes/reales segun su definicion en la base de datos
al "traelos" de nuevo de la base de datos al codigo, volveran formateados, es decir como un numero.
'''
class DBHandlerPrueba:
    #se crea el ARCHIVO BD si no existe y si lo hace lo sincroniza
    def __init__(self,db_path="BD_PRUEBA/BD_PRUEBA.db"):
        self.conn=sqlite3.connect(db_path)
        self.cursor=self.conn.cursor()
    #se crea la tabla "EN BLANCO" de clientes, actualmente tendra uno generico nada mas
    def crear_tabla_clientes(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cliente(
                            dni VARCHAR PRIMARY KEY NOT NULL,
                            nombre VARCHAR NOT NULL,
                            email VARCHAR NOT NULL,
                            telefono VARCHAR NOT NULL
                            )''')
        self.conn.commit()
        pass

    def agregar_cliente(self):
        pass

    def modificar_cliente(self):
        pass

    def eliminar_cliente(self):
        pass

    #se crea la tabla "EN BLANCO" de pedidos, fechas en AAAA/MM/DD
    def crear_tabla_pedido(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pedido(
                            id_pedido VARCHAR PRIMARY KEY,
                            dni_pedido VARCHAR NOT NULL,
                            material TEXT CHECK (material IN('Acrilico','MDF(madera)','Polifan','Otros/varios')),
                            cantidad INTEGER,
                            costo REAL,
                            estado TEXT CHECK (estado IN ('Iniciado','En Proceso','Finalizado','Retirado')),
                            descripcion TEXT,
                            fecha_actual DATE NOT NULL,
                            fecha_entrega DATE NOT NULL,
                            FOREING KEY (dni_pedido) REFERENCES cliente(dni) )
        ''')

        self.conn.commit()
#compruebo si existe un cliente con dicho dni para no duplicar el mismo, me condiciona que, incertar un pedido deba si o si existir en la bd el cliente.
    def comprobar_existencia_cliente(self,dni):
        try:
            self.cursor.execute("SELECT dni FROM cliente WHERE dni=?",(dni,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print(f"cleinte no exixstent {e}")
            #raise ValueError("cliente no registrado")
            return False
    def comprobar_campos(self,dni_pedido,cantidad,costo,adelanto,fecha_entrega,descripcion):
        if not dni_pedido or not re.match(r"r^\d{8}$",dni_pedido):
            raise ValueError("DNI no valido")
        if not cantidad or not re.match(r'^\d+$',cantidad):
            raise ValueError("cantidad ingresada no valida")
        if not costo or not re.match(r"^-?\d+(\.\d+)?$",costo):
            raise ValueError("costo ingresado no valido")
        if not adelanto or not re.match(r"^-?\d+(\.\d+)?$",adelanto):
            raise ValueError("adelanto ingresado no valido")
        if not fecha_entrega or not re.match(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$",fecha_entrega):
            raise ValueError("fecha de entrega no valida, solo se acepta AAAA-MM-DD")
        if not descripcion:
            raise ValueError("descripcion necesaria")
    

    def incertar_pedido(self,id_pedido,dni_pedido,material,cantidad,costo,adelanto,fecha_entrega,estado,descripcion):
        #compruebo que todos los tipos de datos esten correctos
        self.comprobar_campos()#si encuentra un error, interrumpira el proceso
        #no estan vacios entonces incerto si y solo si existe un cliente con el dni incertado
        if self.comprobar_existencia_cliente(dni_pedido):
            try:
                query='''INSERT INTO pedido(id_pedido,dni_pedido,material,cantidad,costo,adelanto,estado,descripcion,fecha_actual,fecha_entrega) VALUES (?,?,?,?,?,?,?,?)'''
                self.cursor.execute(query,str(uuid.uuid4()),dni_pedido,material,cantidad,costo,adelanto,estado,descripcion,datetime('now'),fecha_entrega)
                self.conn.commit()#se guardan los cambios en caso de ser exitoso
            except Exception as e: #al usar try no se interrumpe al generar errores, por lo que tiramos por pantalla el error
                raise ValueError("ERROR EN LA CARGA DE DATOS")
        else:
            raise ValueError("ERROR DNI DEL CLIENTE AUN NO REGISTRADO.") 

    def buscar_pedido(self):
        pass

    def modificar_pedido(self):
        pass

    def eliminar_pedido(self):
        pass

