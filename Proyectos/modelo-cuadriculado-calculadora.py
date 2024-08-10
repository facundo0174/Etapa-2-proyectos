import tkinter 
'''
ACLARACIONES.
se utiliza "entrada_visual=tkinter.entry" ya que es posible "actualizar" los valores borrando e insertando con .delete/.insert(inicio,fin), para el final del
propio objeto se utiliza tkinter.END, que indica el final del mismo, en este caso el ultimi caracter contenido dentro de entrada_visual.


'''

def limpiar_pantalla ():
    entrada_visual.delete(0,tkinter.END)

def colocar_boton(valor_boton):
    valor_pantalla=entrada_visual.get()
    entrada_visual.delete(0,tkinter.END)
    entrada_visual.insert(0,valor_pantalla+valor_boton)

def realizar_operacion():
    try:
        resultado=eval(entrada_visual.get())
        '''
        eval lo que hace es que si es una exprecion matematica pero en strings, lo que ocurre al utilizar por ejemplo inputs por teclado o por botones 
        en este caso, lo que realiza es una conversion obstracta e interpreta de manera numerica si es posible y devuelve el resultado en caso de tenerlo
        de no tenerlo solamente devolvera el contenido numerico o en este caso el contenido que interpreta como numerico tras una conversion, 
        lo devuelve como un integer ademas esto tambien ayuda a exepciones de por ejemplo indeterminaciones como 0 dividido 0.
        '''
        entrada_visual.delete(0,tkinter.END)
        entrada_visual.insert(0,str(resultado))
    except Exception:
        '''
        exception es el valor predeterminado para todas las exepciones de un resultado erroneo de eval(),
        lo que solo dara cuando no sea posible una conversion numerica
        '''
        entrada_visual.delete(0,tkinter.END)
        entrada_visual.insert(0,"ERROR OPERACION NO VALIDA")




ventana=tkinter.Tk()
ventana.title("calculadora basica")

botones=[
    "1","2","3","+",
    "4","5","6","-",
    "7","8","9","*",
    "0",".","/","="]

entrada_visual=tkinter.Entry(ventana,width=30,font=("Arial",30))
entrada_visual.grid(row=0,column=0,columnspan=4)
fila=1
columna=0
for boton_recorrido in botones:#bulce for para recorrer el diccionario e incertar los botones
    if boton_recorrido=="=":
        tkinter.Button(ventana,text=boton_recorrido,command=realizar_operacion).grid(row=fila,column=columna)
    else:
        tkinter.Button(ventana,text=boton_recorrido,command=lambda b=boton_recorrido: colocar_boton(b)).grid(row=fila,column=columna)
        columna+=1
        if columna>3:
            fila+=1
            columna=0
    #termino el for, termino de crear los botones y poscicionarlos, faltaria el CLEAR
tkinter.Button(ventana,text="C",command=limpiar_pantalla).grid(row=fila+1,column=columna)
    
ventana.mainloop()