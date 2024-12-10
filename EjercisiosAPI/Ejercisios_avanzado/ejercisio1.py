import json
import requests

# Función para obtener los personajes de una página específica
def obtener_personajes(pagina):
    url = f"https://rickandmortyapi.com/api/character?page={pagina}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        return respuesta.json()  # Devuelve la respuesta JSON con los personajes
    else:
        print("Error al obtener los datos.")
        return None

# Función principal
def main():
    pagina = 1
    personajes_por_pagina = 5

    while True:
        # Llamamos a la función para obtener los personajes de la página actual
        datos = obtener_personajes(pagina)
        
        if datos:
            # Mostramos los personajes de la página
            print(f"\nPágina {pagina}:")
            total_personajes = datos['info']['count']
            total_personajes_mostrados = 0

            for i in range(personajes_por_pagina):
                # Verificamos si aún hay personajes disponibles en la página
                if total_personajes_mostrados < total_personajes:
                    print(f"{total_personajes_mostrados + 1}. {datos["results"][total_personajes_mostrados]['name']}")
                    total_personajes_mostrados += 1
                else:
                    break  # Si no hay más personajes, salimos del ciclo

            # Preguntamos si el usuario quiere ver más
            respuesta = input("\n¿Quieres ver más? (s/n): ").strip().lower()
            if respuesta != 's':
                print("Gracias por ver los personajes.")
                break  # Si el usuario no quiere continuar, salimos del ciclo

            # Si hemos mostrado todos los personajes disponibles, terminamos
            if total_personajes_mostrados >= total_personajes:
                print("Se han mostrado todos los personajes.")
                break  # Si no hay más personajes, terminamos el ciclo

            # Incrementamos la página para obtener los personajes de la siguiente página
            pagina += 1
        else:
            print("No se pudieron obtener los datos.")
            break

# Llamada a la función principal
main()