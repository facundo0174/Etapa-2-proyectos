#app mentoria
import tkinter as tk
from tkinter import messagebox, simpledialog

from BD_mentoria import DBHandlerNotas

#inicializamos coneccion db
db=DBHandlerNotas()
db.crear_tablas()

'''crea instancia dbhandelr y sellama
al metodo para asgurar que la tabla
de la base de datos esten configuradas
correctamente para su interaccion con la app'''

