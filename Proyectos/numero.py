import random

def adivina():
    numero_magico=random.randint(0,100)
    intentos=0
    max_intentos=6
    numero=999
    print(f"adivina el numero magico tiene {max_intentos} intentos")

    while intentos <= max_intentos and numero!= numero_magico:
        numero=int(input("ingresa un numero entre 1 y 100"))

        if numero == numero_magico:
            print(f'felicidades haz logrado adivinar el numero, era {numero_magico}, lo lograste en {intentos} intentos')
            break
        elif numero < numero_magico:
            print(f'tu numero esta por encima, prueba con otro, te quedam {intentos} intentos')
            intentos+=1
        else:
            print(f'tu numero esta por debajo, prueba con otro, te quedam {intentos} intentos')
            intentos+=1
    if numero==numero_magico:
        print(f" te quedaste sin intentos, haz fallado, el numero era {numero_magico}")

adivina()
