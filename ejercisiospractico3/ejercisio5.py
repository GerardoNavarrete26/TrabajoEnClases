#Pide al usuario un número entero e imprime la tabla de multiplicar de ese número del 1 al 10 utilizando un bucle for.
# Entrada: 3
# Salida:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

numero = int(input("Ingrese el numero para hacer la tabla de multiplicar :"))
hastacuanto = int(input("Ingrese cuantas veces lo quieres multiplicar :"))

for i in range(hastacuanto+1):
    resultado = numero*i
    print(f"{numero} x {i} = {resultado}")