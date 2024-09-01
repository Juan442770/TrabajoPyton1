contraseña = "secreta"
intentos = 0
acceso_correcto = False

while intentos < 3 and not acceso_correcto:
    intento = input("Introduce la contraseña: ")
    if intento == contraseña:
        print("Acceso Correcto")
        acceso_correcto = True
    else:
        intentos += 1

if not acceso_correcto:
    print("El acceso se ha bloqueado después de los 3 intentos")