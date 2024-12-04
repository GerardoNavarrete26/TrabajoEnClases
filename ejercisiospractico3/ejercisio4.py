#Escribe un programa que genere un número aleatorio entre 1 y 20 y permita al usuario adivinarlo. El programa debe darle pistas si el número es mayor o menor al número a adivinar, utilizando un bucle while.
# Entrada: 10
# Pista: El número es menor.


#importar libreria randoms
import random
#Genera un numero random y lo guarda en la variable
adivinarnumero = random.randint(1, 20)
adivinado = False

print("Adivina el número (entre 1 y 20):")

#el not es como decir  while adivinado == false:
while not adivinado:
   
    intento = int(input("Cual crees que es? : "))
    
    
    if intento < adivinarnumero:
        print("El número es mayor.")
    elif intento > adivinarnumero:
        print("El número es menor.")
    else:
        print(f"¡Felicidades! Adivinaste el número es: {adivinarnumero}")
        adivinado = True