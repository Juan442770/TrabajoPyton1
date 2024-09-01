numero = int(input("Introduce un número entero: "))

print(f"El número {numero} cumple los siguientes criterios de divisibilidad:")

if numero % 2 == 0:
    print("- Es divisible por 2")

suma_digitos = 0
for digito in str(numero):
    suma_digitos += int(digito)
if suma_digitos % 3 == 0:
    print("- Es divisible por 3")

if str(numero).endswith('0') or str(numero).endswith('5'):
    print("- Es divisible por 5")

if numero % 2 == 0 and suma_digitos % 3 == 0:
    print("- Es divisible por 6")

if suma_digitos % 9 == 0:
    print("- Es divisible por 9")

if str(numero).endswith('0'):
    print("- Es divisible por 10")