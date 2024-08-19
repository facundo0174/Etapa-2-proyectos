#Importaciones
import re
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox

#Configuración de la ventana principal                
root = Tk()
root.title("Calculadora Basica")
root.configure(bg="#F5CA7B")
#Configuración del marco
frm = ttk.Frame(root, padding=10)
frm.grid(row=0,column=0)

#Etiqueta
#ttk.Label(frm, text="Ingrese la operacion",font=("Arial",15)).grid(column=0, row=0,padx=2,pady=2) 

#Campo de entrada 
entrada_nombre = Entry(root, width=50,justify=CENTER,font=("Arial",25) )
entrada_nombre.grid(column=0,row=0,columnspan=4)

#Botones de los operadores 
operadores = ['+','-','*','/','.']

fila=1

for operador in operadores:
    bot_ope = Button(root, text=operador,font=("Arial",15),height=3,width=15,bg="#FF77FF", command=lambda operador=operador: entrada_nombre.insert(END,operador))
    bot_ope.grid(row=fila, column=(0), padx=1, pady=5)
    fila+=1


#Botones de los numeros 
numeros = ['9','8','7','6','5','4','3','2','1','0']

fila=1
columna=1

for num in numeros :
    if num=="0":
        bot_num = Button(root, text= num,font=("Arial",15),height=3,width=36,bg="light blue", command=lambda num=num: entrada_nombre.insert(END, num) )
        bot_num.grid(row = 4, column=1,columnspan=2, padx=2,pady=2)
    else:
        bot_num = Button(root, text= num,font=("Arial",15),height=3,width=15,bg="light blue", command=lambda num=num: entrada_nombre.insert(END, num) )
        bot_num.grid(row = fila, column=columna, padx=2,pady=2)

    if columna>3 and num!="0":
        columna=1
        fila+=1
        bot_num.grid(row = fila, column=columna, padx=2,pady=2)
    columna+=1

#Funcion para calcular la operacion                
def calcular():
    try:
        expresion = entrada_nombre.get()
        expresionsin_ceros = re.sub(r'\b0+(\d)', r'\1', expresion)
        resultado = eval(expresionsin_ceros) 
        messagebox.showinfo("Resultado", f"Resultado: {resultado}")
    except:
        entrada_nombre.delete(0, END)  
        entrada_nombre.insert(END, "ERROR" ) 
        messagebox.showerror(title="Error", message="Operacion matematica no valida", icon='error')

# Llamar a la función calcular cuando se presiona Enter
def on (event):
    calcular()

#Vincular a la funcion evento 
entrada_nombre.bind("<Return>", on)

#Boton =
def borrar_todo():
    entrada_nombre.delete(0,END)

def borrar():
    contenido=entrada_nombre.get()
    if contenido:
        entrada_nombre.delete(len(contenido)-1)

boton2 = Button(root, text="C",font=("Arial",15),height=3,width=15,bg="pink", command=borrar_todo)
boton2.grid(column=1,row=5)

boton1 = Button(root, text="=",font=("Arial",15),height=7,width=15,bg="light green", command=calcular )
boton1.grid(column=3,row=4,rowspan=5)

boton3 = Button(root, text="<",font=("Arial",15),height=3,width=15,bg="pink", command=borrar )
boton3.grid(column=2,row=5)



#Iniciar el bucle principal de la interfaz gráfica
root.mainloop()