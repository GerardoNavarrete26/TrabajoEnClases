lista_numero = []
cantidad = int(input("Ingrese cuanto numero queires guardar :"))
for  i in range(cantidad) : 
    numero = int(input(f"Introduce el número {i + 1}: "))
    if numero%2 == 0:
        lista_numero.append(numero)
  
print(f"La lista de numero pares 6es : {lista_numero}")