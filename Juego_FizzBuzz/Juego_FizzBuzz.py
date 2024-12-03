cantidad = int(input("Ingresa Cantidad de numeros para el juego: "))


for numero in range(1, cantidad + 1):
   
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"Fizz Buzz")
   
    elif numero % 3 == 0:
        print(f"Fizz")
    
    elif numero % 5 == 0:
        print(f"Buzz")
    # Si no cumple ninguna de las condiciones anteriores, imprimir el número y su rango
    else:
        print(f"{numero}")