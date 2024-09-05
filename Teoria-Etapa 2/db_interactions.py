import sqlite3
import uuid
import datetime
import re


class DBHandler:
    def __init__(self, db_path="db/app_tkinter.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def crear_tablas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                          id VARCHAR PRIMARY KEY,
                          username VARCHAR NOT NULL,
                          email VARCHAR NOT NULL,
                          password BLOB NOT NULL,
                          created_at TIMESTAMP NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                          id VARCHAR PRIMARY KEY,
                          usuario_id VARCHAR NOT NULL,
                          titulo VARCHAR NOT NULL,
                          contenido TEXT NOT NULL,
                          created_at TIMESTAMP NOT NULL,
                          FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
                          id VARCHAR PRIMARY KEY,
                          nombre VARCHAR NOT NULL,
                          created_at TIMESTAMP NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts_categorias (
                          post_id VARCHAR NOT NULL,
                          categoria_id VARCHAR NOT NULL,
                          FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
                          FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE,
                          PRIMARY KEY (post_id, categoria_id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS comentarios (
                          id VARCHAR PRIMARY KEY,
                          usuario_id VARCHAR NOT NULL,
                          post_id VARCHAR NOT NULL,
                          contenido TEXT NOT NULL,
                          created_at TIMESTAMP NOT NULL,
                          FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                          FOREIGN KEY (post_id) REFERENCES posts(id))''')

        self.conn.commit()

    def insertar_usuario(self, username, email, password):
        password = password.encode('utf-8')

        if not username or len(username) > 50:
            raise ValueError(
                "El nombre de usuario no puede estar vacio o no puede superar los 50 caracteres")

        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("El correo electronico no es valio")

        if len(password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

        self.cursor.execute(
            "SELECT id FROM usuarios WHERE email = ?", (email,))

        if self.cursor.fetchone():
            raise ValueError(
                "Ya existe un usuario con este correo electronico")

        query = f'''INSERT INTO usuarios (id, username, email, password, created_at)
            VALUES (?, ?, ?, ?, ?)'''

        self.cursor.execute(query, (str(uuid.uuid4()), username, email,
                                    password, datetime.datetime.now()))

        self.conn.commit()

    def login_usuario(self, email, password):
        pass
