import sqlite3
import uuid #modulo de objetos permite funciones 
import datetime

class DBHandlerPrueba:
    def __init__(self,db_path="BD_PRUEBA/BD_PRUEBA.db"):
        self.conn=sqlite3.connect(db_path)
        self.cursor=self.conn.cursor()
    
    def crear_tabla_pedido(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pedido(
                            id_pedido VARCHAR PRIMARY KEY,
                            costo REAL NOT NULL,
                            cantidad INTEGER NOT NULL
                            estado TEXT CHECK (estado IN ('Iniciado','En Proceso','Finalizado','Retirado')) NOT NULL,
                            descripcion TEXT NOT NULL
                            fecha_actual TEXT DEFAULT (datetime('now')),
                            fecha_entrega TEXT)

        ''')
        pass

    def incertar_pedido(self):
        pass

    def buscar_pedido(self):
        pass

    def modificar_pedido(self):
        pass

    def eliminar_pedido(self):
        pass

