def finabocci (tope):
    resg1=0
    resg2=1
    orden=1
    if tope <= 0 :
        print('error se ingreso un orden menor o igual a 0')
    else:
        while orden<tope:
            print( "finabocci de orden "n," es igual a: "resg1+resg2)
            orden+=1
            resg1+=1
            resg2+=1

tope=input(int("ingrese el numero de orden fibonacci"))
finabocci(tope)



--------------------
def generar_fibonacci(limite):
    """
    Genera la serie de Fibonacci hasta un límite establecido por el usuario.

    :param limite: El valor límite hasta el cual se generará la serie de Fibonacci.
    :return: Una lista con los números de la serie de Fibonacci hasta el límite.
    """
    if limite < 0:
        return "El límite debe ser un número no negativo."

    fibonacci = [0, 1]
    siguiente = fibonacci[-1] + fibonacci[-2]
    while siguiente <= limite:
        fibonacci.append(siguiente)
        siguiente = fibonacci[-1] + fibonacci[-2]

    return fibonacci

----------