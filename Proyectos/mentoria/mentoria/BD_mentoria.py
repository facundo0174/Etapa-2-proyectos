#BD mentoria
import sqlite3
import uuid #modulo de objetos permite funciones 
import datetime

class DBHandlerNotas:
    def __init__(self,db_path='mentoria/app_mentoria.db'):
        self.conn=sqlite3.connect(db_path)
        self.cursor=self.conn.cursor()

    def crear_tablas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usiuarios(
                            id VARCHAR PRIMARY KEY,
                            username VARCHAR NOT NULL UNIQUE,
                            password VARCHAR NOT NULL,
                            created_at TIMESTAMP NOT NULL
                            )
                            ''')#se escribe adentro lo que se quiera  crear en la bd
        self.cursor.execute('''CREATE TABLE IF NOT EXIST notas(
                            id VARCHAR PRIMARY KEY,
                            usuari_id VARCHAR NOT NULL,
                            titulo VARCHAR NOT NULL,
                            contenido TEXT NOT NULL,
                            created_at TIMESTAMP NOT NULL,
                            FOREIGN KEY (usuario_id) REFERENCES usuarios(id))
                        ''')
        
        self.conn.commit()

        def insertar_usuario(self,username,password):
            if not username or not password:
                raise ValueError("el nombre de usuario o la contrasenia son obligarios")
            
            try:
                query =''' INSERT INTO  usuarios(id,username,password,created_at) VALUES (?,?,?,?)'''
                self.cursor.execute(query,(str(uuid.uuid4(), username,password,datetime.datetime.now())))
            except sqlite3.IntegrityError:
                raise ValueError("el nombre de usuario ya existe")
        
        def login_usuario(self,username,password):
            query="SELECT id FROM usuarios WHERE username = ? AND password = ?"
            self.cursor.execute(query,(username,password))
            usuario =self.cursor.fechone()#fila por fila recorre
            if usuario:
                return usuario[0]
            else:
                raise ValueError("nombre de usuario o contraseña incorrectos")
        
        def incertar_notas(self,usuario_id,titulo,contenido):
            if not titulo or not contenido:
                raise ValueError("el titulo y contenido son obligatorios")
            query = '''INSERT INTO notas(id,usuario_id,titulo,contenido,created_at) VALUES(?,?,?,?,?)'''
            self.cursor.execute(query,(str(uuid.uuid4(),usuario_id,titulo,contenido,datetime.datetime.now())))
            self.conn.commit()
