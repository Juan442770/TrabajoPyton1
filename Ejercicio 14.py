import random

numero_aleatorio = random.randint(0, 100)
intentos = 0

while True:
    numero = int(input())
    intentos += 1

    if numero < numero_aleatorio:
        print("Es muy bajo")
    elif numero > numero_aleatorio:
        print("Es muy alto")
    else:
        print(f"Correcto, número encontrado. Cantidad de intentos: {intentos}")
        break