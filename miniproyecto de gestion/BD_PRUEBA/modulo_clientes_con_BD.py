import sqlite3
import uuid
import datetime

class DBmisclientes:
    def init(self, db_path="db/appclientes.db"): 
        self.conn=sqlite3.connect(db_path)
        self.cursor=self.conn.cursor
    def crear_tablas(self):
        self.cursor.execute("""CREATE TABLE if NOT EXISTS clientes(dni VARCHAR PRIMARY KEY, nombre VARCHAR NOT NULL, domicilio VARCHAR NOT NULL, create_at TIMESTAMP NOT NULL)""")
        self.conn.commit()

def insertar_cliente(self, dni, nombre, domicilio, create_at ):
    if not dni or not nombre:
        raise ValueError ("el dni y el nombre son obligatorios")
    try :
        query="INSERT INTO clientes(dni, nombre, domicilio, create_at) VALUES (?,?,?,?)"
        self.cursoe.execute(query,(str(uuid.uuid4(),nombre, domicilio, create_at )))
        self.conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("el nombre y dni ya existen ")# aca no se como seria si un cliente quiere hacerme dos compras

def nuevo_cliente (self, dni, nombre, domicilio, create_at):
    query="SELECT id FROM clientes WHERE dni=? AND nombre=? "
    self.cursor.fetchone()
    if nombre:
        return nombre[0]
    else:
        raise ValueError("nombre incorrecto")