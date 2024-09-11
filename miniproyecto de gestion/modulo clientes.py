#modulo clientes
import tkinter as tk
from tkinter import Label, Button, Entry, Listbox
#Listbox es un componente de tkinter para listas

ventana=tk.Tk()
ventana.title("Alta, baja modificacion de clientes")
ventana.geometry("400x400")

def clientes(): #metono define clientes y los agrega a lista
    cliente_n=texto1.get()
    cliente_t=texto2.get()
    cliente_d=texto3.get()

    mi_cliente.insert(tk.END, f"{cliente_n} - {cliente_t} - {cliente_d}")

def nuevo_cliente():
    texto1.delete(0, tk.END) 
    texto2.delete(0, tk.END)#ejecuta el codigo y fijate, asi tendrías que hacer con cada una de las variables "texto"
    texto3.delete(0, tk.END) 
    mi_cliente.delete(tk.END, 0 )  # silvi, quiero borrar los campos , al momento de apretar este boton, no me funciona

def eliminar_cliente():
    seleccion = mi_cliente.curselection()
    """mi_cliente.curselection() devuelve una tupla con el índice del elemento 
    actualmente seleccionado en el Listbox. Si no hay ningún elemento seleccionado, devuelve una tupla vacía.
    """
    if seleccion: 
        """comprueba si la tupla no está vacía. Si hay una selección, seleccion contendrá al menos un índice. Si no hay selección, la tupla estará vacía."""
        mi_cliente.delete(seleccion[0])
        """elimina el elemento del Listbox en el índice especificado. seleccion[0] es el primer (y único) índice en la tupla de selección"""
    else:
       print("seleccione") #algun mensaje que diga "error, seleccione un cliente"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

def modificar_cliente():
    seleccion = mi_cliente.curselection()
    if seleccion:
        cliente_info = mi_cliente.get(seleccion[0]).split(" - ")
        """mi_cliente.get(seleccion[0]) obtiene el texto del cliente en el índice seleccionado.
        .split(" - ") divide este texto en una lista de tres partes, basándose en el delimitador " - ". Esto supone que el formato del texto en la lista es "Nombre - Teléfono - Dirección".
        """

        texto1.delete(0, tk.END)
        texto1.insert(0, cliente_info[0])
        #realizar las mismas funciones que le hicimos a texto1, a texto2 y texto3

        mi_cliente.delete(seleccion[0])
    else:
        print("seleccione")# "error, seleccione un cliente"

label1=Label(ventana, text ="Nombre de cliente", bg="yellow") # label ingresa nombre de cte
label1.place(x=10, y=10, width=100, height=30) 
texto1=Entry(ventana, bg="pink")
texto1.place(x=120, y =10, width=100, height=30)


label2=Label(ventana, text ="Telefono de cliente", bg="yellow")# tel de cliente
label2.place(x=10, y=50, width=100, height=30)


texto2=Entry(ventana, bg="pink")
texto2.place(x=120, y =50, width=100, height=30)
label3=Label(ventana, text ="Direccion de cliente", bg="yellow") # direccion de cliente
label3.place(x=10, y=90, width=100, height=30)

texto3=Entry(ventana, bg="pink")  #espacio para los clientes cargados
texto3.place(x=120, y =90, width=100, height=30)

label4=Label(ventana, text ="Clientes", bg="blue", fg="white") # muestra lista de cliente luego de apretar boton
label4.place(x=10, y=130, width=100, height=30)
label2=Label(ventana, text ="Telefono de cliente", bg="yellow")# tel de cliente
label2.place(x=10, y=50, width=100, height=30)


texto2=Entry(ventana, bg="pink")
texto2.place(x=120, y =50, width=100, height=30)
label3=Label(ventana, text ="Direccion de cliente", bg="yellow") # direccion de cliente
label3.place(x=10, y=90, width=100, height=30)

texto3=Entry(ventana, bg="pink")#corregido pinck a pink
texto3.place(x=120, y =90, width=100, height=30)

label4=Label(ventana, text ="Clientes", bg="blue", fg="white" )# muestra lista de cliente luego de apretar boton
label4.place(x=10, y=130, width=100, height=30)

mi_cliente=Listbox(ventana, bg="pink")

mi_cliente.place(x=120, y =130, width=250, height=60)


boton1=Button(ventana, text="Cargar cliente", command=clientes, bg="light pink") #boton muestra clientes 
boton1.place(x=230, y = 190, width=100, height=30)
boton2=Button(ventana, text="Agregar nuevo cte ", command=nuevo_cliente, bg="light pink")
boton2.place(x=230, y = 230, width=150, height=30)
boton3=Button(ventana, text="modificar ", command=modificar_cliente, bg="light pink")
boton3.place(x=230, y = 270, width=150, height=30)
boton4=Button(ventana, text="eliminar ", command=eliminar_cliente, bg="light pink")
boton4.place(x=230, y = 310, width=150, height=30)

ventana.mainloop()