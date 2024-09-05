import tkinter as tk
from tkinter import messagebox
from db_interactions import DBHandler


db = DBHandler()
db.crear_tablas()


class BlogApp():
    def __init__(self):
        self.usuario_logueado = None
        self.mostrar_login()

    # Metodos usados en las ventanas (acciones)
    def limpiar_campos(self, *campos):
        for campo in campos:
            if campo is not None:
                campo.delete(0, tk.END)

    def ui_login(self):
        pass

    def ui_insertar_usuario(self, campo_username, campo_email, campo_password, ventana_registro):
        username = campo_username.get().strip()
        email = campo_email.get().strip()
        password = campo_password.get().strip()

        if not username or not email or not password:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            try:
                db.insertar_usuario(username, email, password)
                messagebox.showinfo("Exito", "Usuario registrado con exito!")
                self.limpiar_campos(
                    campo_username, campo_email, campo_password)
                ventana_registro.destroy()
            except ValueError as e:
                messagebox.showerror("Error al registrar usuario", str(e))

    def ui_listar_posts(self, lista_posts):
        pass

    def ui_mostrar_post(self):
        pass

    def ui_insertar_post(self):
        pass

    # Metodos que definen y muentran la ventana
    def mostrar_registro(self):
        ventana_registro = tk.Tk()
        ventana_registro.title('Registro')
        ventana_registro.geometry('400x400')

        tk.Label(ventana_registro, text="Nombre de Usuario").pack(pady=10)
        campo_username = tk.Entry(ventana_registro, width=50)
        campo_username.pack(pady=5)

        tk.Label(ventana_registro, text="Email").pack(pady=10)
        campo_email = tk.Entry(ventana_registro, width=50)
        campo_email.pack(pady=5)

        tk.Label(ventana_registro, text="Contraseña").pack(pady=10)
        campo_password = tk.Entry(ventana_registro, width=50, show='*')
        campo_password.pack(pady=5)

        boton_registrar = tk.Button(ventana_registro, text="Registrar",
                                    command=lambda: self.ui_insertar_usuario(campo_username, campo_email, campo_password, ventana_registro))
        boton_registrar.pack(pady=20)

        ventana_registro.mainloop()

    def mostrar_login(self):
        ventana_login = tk.Tk()
        ventana_login.title('Login')
        ventana_login.geometry('400x300')

        tk.Label(ventana_login, text="Email").pack(pady=10)
        campo_email_login = tk.Entry(ventana_login, width=50)
        campo_email_login.pack(pady=5)

        tk.Label(ventana_login, text="Contraseña").pack(pady=10)
        campo_password_login = tk.Entry(ventana_login, width=50, show='*')
        campo_password_login.pack(pady=5)

        boton_login = tk.Button(ventana_login, text="Login",
                                command=lambda: self.ui_login(campo_email_login, campo_password_login, ventana_login))
        boton_login.pack(pady=10)

        boton_registro = tk.Button(
            ventana_login, text="Registrar", command=self.mostrar_registro)
        boton_registro.pack(pady=10)

        ventana_login.mainloop()

    def mostrar_pagina_principal(self):
        ventana_principal = tk.Tk()
        ventana_principal.title(
            f'Aplicación de Blog - Usuario ID: {self.usuario_logueado}')
        ventana_principal.geometry('1080x720')
        tk.Label(ventana_principal, text="Insertar Post").pack(pady=10)

        campo_titulo_post = tk.Entry(ventana_principal, width=50)
        campo_titulo_post.pack(pady=5)
        campo_titulo_post.insert(0, "Título del Post")

        campo_contenido_post = tk.Entry(ventana_principal, width=50)
        campo_contenido_post.pack(pady=5)
        campo_contenido_post.insert(0, "Contenido del Post")

        lista_posts = tk.Listbox(ventana_principal, width=80, height=15)
        lista_posts.pack(pady=5)
        self.ui_listar_posts(lista_posts)

        lista_posts.bind(
            "<Double-1>", lambda event: self.ui_mostrar_post(event, lista_posts))

        boton_insertar_post = tk.Button(ventana_principal, text="Insertar Post",
                                        command=lambda: self.ui_insertar_post(campo_titulo_post, campo_contenido_post, lista_posts))
        boton_insertar_post.pack(pady=10)
        boton_listar_posts = tk.Button(ventana_principal, text="Listar Posts",
                                       command=lambda: self.ui_listar_posts(lista_posts))
        boton_listar_posts.pack(pady=10)

        ventana_principal.mainloop()


app = BlogApp()
