#Ejercicio: Clasificador de edades
#Crea un programa que permita al usuario clasificar edades en diferentes categorías: niño, adolescente, adulto o adulto mayor. El programa debe usar un bucle while para procesar múltiples edades, y condicionales para determinar la categoría correspondiente.
#Instrucciones:
#Pregunta al usuario cuántas edades desea clasificar.
#Usa un bucle while para ingresar las edades una por una.
#Clasifica cada edad según las siguientes reglas:
#Menos de 13 años: Niño.
#Entre 13 y 17 años: Adolescente.
#Entre 18 y 59 años: Adulto.
#60 años o más: Adulto mayor.
#Al finalizar, muestra un resumen indicando cuántas personas hay en cada categoría.
#Al final, pregunta si desea clasificar más edades o salir del programa.



while True:
         
         ninos = 0
         adolescentes = 0
         adultos = 0
         adultos_mayores = 0   
         cantidad = int(input("Cuantas edades quieres ingresar :"))

         for i in range(cantidad):
                edad = int(input(f"Ingrese la edad de la persona {i+1}: "))

                if edad < 13:
                   ninos = ninos + 1
                   print("Categoria : Niño")
                elif 13 <= edad <= 17:
                   adolescentes = adolescentes + 1
                   print("Categoria : Adolecente")
                elif 18 <= edad <= 59:
                   adultos = adultos + 1
                   print("Categoria : Adulto")
                else:
                   adultos_mayores = adultos_mayores + 1
                   print("Categoria : Adulto Mayor")

         print("Resumen de clasificación:")
         print(f"Niños: {ninos}")
         print(f"Adolescentes: {adolescentes}")
         print(f"Adultos: {adultos}")
         print(f"Adultos mayores: {adultos_mayores}")
    
    
         respuesta = input(" Quieres ingresar las edades de nuevo? (si/no): ").lower()
         if respuesta != "si":       
           print("Gracias por usar el programa.")
           break