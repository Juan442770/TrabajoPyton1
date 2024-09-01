
while True:
    dia = int(input())

    if dia < 1 or dia > 7:
        continue

    if dia == 1:
        print("El lunes es un día laboral.")
    elif dia == 2:
        print("El martes es un día laboral.")
    elif dia == 3:
        print("El miércoles es un día laboral.")
    elif dia == 4:
        print("El jueves es un día laboral.")
    elif dia == 5:
        print("El viernes es un día laboral.")
    elif dia == 6:
        print("El sábado no es un día laboral.")
    elif dia == 7:
        print("El domingo no es un día laboral.")
    
    break