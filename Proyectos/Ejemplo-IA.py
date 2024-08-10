import tkinter as tk

def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + valor)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def limpiar():
    entrada.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora Básica")

entrada = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        tk.Button(root, text=boton, width=5, height=2, command=calcular).grid(row=fila, column=columna)
    else:
        tk.Button(root, text=boton, width=5, height=2, command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

tk.Button(root, text="C", width=5, height=2, command=limpiar).grid(row=fila, column=columna)

root.mainloop()
