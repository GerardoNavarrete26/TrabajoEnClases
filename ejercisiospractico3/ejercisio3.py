#Usa un bucle for para calcular la suma de todos los números pares entre 1 y 50 e imprime el resultado.
# La suma de los números pares entre 1 y 50 es: 650
suma = 0
i = 1
rango = int(input("Ingrese el rango de numero que quiere sumar :"))
for  i in range(rango+1) : 
    if i%2 == 0:
       suma = suma + i
print(f"La suma de los pares del rango es : {suma}")