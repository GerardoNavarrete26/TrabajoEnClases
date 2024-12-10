#Ejercicio: Calculadora de áreas

#Crea un programa que permita al usuario calcular el área de una figura geométrica (cuadrado, rectángulo o triángulo). El programa debe usar un bucle while para que el usuario pueda realizar múltiples cálculos y condicionales para determinar la figura seleccionada.
#Instrucciones:
#Pregunta al usuario qué figura desea calcular: cuadrado, rectángulo o triángulo.
#Según la opción, solicita los valores necesarios para el cálculo:
#Para el cuadrado, pide el lado.
#Para el rectángulo, pide la base y la altura.
#Para el triángulo, pide la base y la altura (y recuerda dividir el producto por 2).
#Muestra el área calculada.
#Al final de cada cálculo, pregunta si desea realizar otro cálculo o terminar el programa (usa la palabra "salir" para finalizar el bucle).

while True:
    figura = input("¿Qué figura quieres calcular? (cuadrado/rectángulo/triángulo): ").lower()

    if figura == "cuadrado":
        lado = float(input("Ingresa el valor del lado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")

    elif figura == "rectángulo":
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")

    elif figura == "triángulo":
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")

    else:
        print("Figura no válida, por favor elige entre cuadrado, rectángulo o triángulo.")

    continuar = input("¿Quieres realizar otro cálculo? (sí/salir): ").lower()
    if continuar == "salir":
        break