lista_notas = []
suma = 0
cantidad = 0

while True:
    nota_usuario = input("Introduce una nota o escribe 'fin' para terminar: ")
    if nota_usuario.lower() == 'fin':
        break
    try:
        # Hacemos que la variable nota_usuario sea un float ahora ya que las nota peuden ser 6.5
        nota = float(nota_usuario)
        # Validación que la nota sea real 0-7
        if 0 <= nota <= 7:  
            lista_notas.append(nota)
            suma = suma + nota
            cantidad = cantidad + 1
        else:
            print("La nota debe estar entre 0 y 7")
    except ValueError:
        print("Por favor, introduce un número válido o 'fin'.")


if cantidad > 0:
    promedio = suma / cantidad
    print(f"El promedio es: {promedio:.1f}")
    if promedio >= 4.0:
        print("¡Aprobaste!")
    else:
        print("Reprobaste")
else:
    print("No se ingresaron notas")