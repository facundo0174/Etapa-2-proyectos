import tkinter


def calcular():
  aux = pantalla_visual.get()
  try:
    resultado = eval(aux)
    resultado_visual.delete(0, tkinter.END)
    resultado_visual.insert(0, resultado)
  except Exception:
    resultado_visual.delete(0, tkinter.END)
    resultado_visual.insert(0, "Error operacion no valida, intente nuevamente")


ventana = tkinter.Tk()
ventana.title("Proyecto Informatorio")
ventana.geometry("500x150")

etiqueta = tkinter.Label(ventana, text="Ingrese la expresion matematica ")
etiqueta.pack()

pantalla_visual = tkinter.Entry(ventana)
pantalla_visual.pack()

boton1 = tkinter.Button(ventana, text="Calcular", command=calcular)
boton1.pack()

resultado_visual = tkinter.Entry(ventana, width=42)
resultado_visual.pack()

tkinter.Label(ventana,text=" Soporta operaciones suma(+) resta(-) multiplicacion(*) division(/) y potencia(**)").pack()

ventana.mainloop()
