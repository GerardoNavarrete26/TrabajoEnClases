#Escribe un programa que pida al usuario un número y use una sentencia if-else para determinar si el número es positivo, negativo o cero.
# Entrada: -3
# Salida: El número es negativo.

numero = int(input("Ingrese el numero a indetificar :"))
if numero < 0:
    print("El número es negativo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es positivo.")