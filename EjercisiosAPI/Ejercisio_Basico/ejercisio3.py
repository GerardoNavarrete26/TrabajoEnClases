import requests
import json

def obtener_datos():
        url = "https://api.breakingbadquotes.xyz/v1/quotes"
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
           datos = respuesta.json()
        return datos
def main ():
    while True:
           
           datos = obtener_datos()
           print(f"Frase : {datos[0]['quote']}")
           print(f"Autor : {datos[0]['author']}")
            
           # Preguntamos si el usuario quiere ver más
           respuesta = input("\n¿Quieres ver más? (s/n): ").strip().lower()
           if respuesta != 's':
              print("Gracias por ver los personajes.")
              break  # Si el usuario no quiere continuar, salimos del ciclo

main()