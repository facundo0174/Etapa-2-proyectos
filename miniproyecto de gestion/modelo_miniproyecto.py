import tkinter as tk
import time
ventana = tk.Tk()
ventana.title('Lista de pedidos a realizar')
ventana.geometry('400x200')
reloj= tk.Label(ventana, font=("arial", 10), bg="red", fg="white")
ingreso_tarea = tk.Entry(ventana)
ingreso_tarea.pack()
def hora():
   tiempo_actual=time.strftime("%H")
   reloj.config(text=tiempo_actual)
   ventana.after(1000, hora)
reloj.pack(anchor="center")
hora()
def agregar_tarea():
   tarea = ingreso_tarea.get()
   if tarea:
       lista_tareas.insert(tk.END, tarea)
ingreso_tarea.delete(0, tk.END)
boton_agregar = tk.Button(ventana, text = 'Agregar Pedido', command = agregar_tarea, bg="green")
boton_agregar.pack()
def eliminar_tarea():
 seleccion = lista_tareas.curselection()
 if seleccion:
   lista_tareas.delete(seleccion)
boton_eliminar = tk.Button(ventana, text = 'Eliminar Pedido', command = eliminar_tarea, bg="pink")
boton_eliminar.pack()
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()
ventana.mainloop()