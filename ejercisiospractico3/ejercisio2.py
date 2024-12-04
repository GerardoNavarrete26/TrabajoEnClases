#Escribe un programa que utilice un bucle while para imprimir los números del 10 al 1 en orden descendente.
# Salida:
# 10
# 9
# 8
# ...
# 1

numero = int(input("Ingrese cuanto numero queires mostrar :"))
while  numero >= 1: 
    print(f"#{numero}")
    numero = numero -1