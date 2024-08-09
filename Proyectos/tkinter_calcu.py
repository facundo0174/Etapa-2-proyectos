import tkinter

def suma():
    a=int(input("ingrese el primer sumando \n"))
    b=int(input("ingrese el segundo sumando \n"))
    return(a+b)

def resta():
    a=int(input("ingrese el minuendo \n"))
    b=int(input("ingrese el sustraendo \n"))
    return(a-b)

def multiplicacion ():
    a=int(input("ingrese el multiplicando \n"))
    b=int(input("ingrese el multiplicador \n"))
    return(a*b)

def division ():
    a=int(input("ingrese el dividendo \n"))
    b=int(input("ingrese el divisor \n"))
    return(a/b)

def saludar():
    print("saludar")

def intput_ui():
    #asegurarse de que sean variables globales de lo contrario no modificara para utilizarce en el main
    num1=cajatexto.get() #traigo lo que se ingreso, pero asegurarse del tipo de dato
    #etc etc


num1=0
num2=0
''' la idea en este momento es utilizar estas variables globales para luego pasarlas a las funciones que retornen
la operacion matematica ya que las operaciones se realizan con variables locales y devuelven el resultado'''

#creacion de la UI mediante la definicion de un objeto con la libreria, un titulo reprecentativo y su geometria visible
ventana = tkinter.Tk()
ventana.title("Calculadora UI")
ventana.geometry("500x500")

#ejemplo de creaccion de subtitulos en dentro de la UI
subtitulo=tkinter.Label(ventana,text="Elija una operacion matematica.") #los parametros siempre son (a quien pertenece o dentro de quien, accion/tipo de incersion) en este caso es texto
'''
puedes colocar ,padx:numero,pady:numero, para jugar con las coordenadas posicionales del subtitulo/etiqueta, estas  coordenadas tienen como (0,0) la 
esquina superior izquierda del objeto contenedor en este caso la variable ventana, sin embargo aumentado en 4 en ambos, ya que posee un espacio reservado
para el titulo "Calculadora IU" asi como botones de una ventana comun y corriente como ser el de salida, minimizacion. por lo tanto el (0,0) seria el (4,4)
el programa obvia esto, es decir nos abstrae la idea de conocer la coordenada exacta con o sin suma, pero no todos los lenguajes lo hacen.
'''
subtitulo.grid(row=0,column=2) #pack lo incerta dentro del objeto ventana de manera visible
#boton1 de prueba el resto no hace nada solo es texto
boton1=tkinter.Button(ventana,text="Suma de 2 numeros",command=saludar)
boton1.grid (row=1, column=0)
#boton1.pack()
boton2=tkinter.Button(ventana,text="Resta de 2 numeros")
boton2.grid(row=2, column=0)
#boton2.pack()
boton3=tkinter.Button(ventana,text="Multiplicacion de 2 numeros")
boton3.grid(row=3, column=0)
#boton3.pack()
boton4=tkinter.Button(ventana,text="Division de 2 numeros")
boton4.grid(row=4, column=0)
#boton4.pack() 

#caja de texto como input dentro de la ventana, se le puede colocar fuentes y texto
cajatexto=tkinter.Entry(ventana)
cajatexto.grid(row=1,column=2)

'''
creacion de un boton que se "enlaza" con la caja de texto a utilizar, y a su vez recupera
el valor ingresado para realizar algun tipo de accion despues  con ello, recordar comprobar el tipo de dato final de la recuperacion
'''
boton_input=tkinter.Button(ventana,text="Ingresar",command=intput_ui)
boton_input.grid(row=2, column=2)



ventana.mainloop()#bucle infinito que termina mediante interaccion de usuario


"""
esto puede servir a futuro para la recuperacion y conversion de datos
ingresados por pantalla


entrada = input("Ingresa un número: ")
try:
    numero_entero = int(entrada)
    print(f"El número ingresado como entero es: {numero_entero}")
except ValueError:
    print("El valor ingresado no es un número válido.")

"""