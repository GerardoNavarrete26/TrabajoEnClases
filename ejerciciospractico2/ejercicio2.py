lista_numero = []
cantidad = int(input("Ingrese cuanto numero queires guardar :"))
resultado = 0
contador = 1
while  contador <= cantidad: 
    numero = int(input(f"Ingrese el numero {contador}  queires guardar :"))
    lista_numero.append(numero)
    contador = contador +1
    resultado = resultado + numero
print(f"Los numero de la lista sumados son : {lista_numero}")
print(f"La suma de los elemento es : {resultado}")