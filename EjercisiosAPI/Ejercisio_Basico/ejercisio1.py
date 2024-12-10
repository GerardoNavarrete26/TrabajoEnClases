
import requests

def obtener_lista_razas():
    url = "https://dog.ceo/api/breeds/list/all"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
    return datos["message"]

def mostrar_razas(razas):
    print("Lista de razas disponibles:")
    for indice, raza in enumerate(razas, start=1):  # El índice comienza en 1
        print(f"{indice}. {raza}")

def main():
    razas = obtener_lista_razas()

    if razas:
        mostrar_razas(razas)
    else:
        print("No se pudo obtener la lista de razas.")

if __name__ == "__main__":
    main()