import requests
import json

def obtener_latlog(ciudad):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()  # Devuelve la respuesta JSON con los personajes
    else:
        print("Error al obtener los datos.")
        return None
    
def mostrar_datos_ciudad(lat,lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()  # Devuelve la respuesta JSON con los personajes
    else:
        print("Error al obtener los datos.")
        return None


def main():
    ciudad = input("Ingresa una ciudad :")
    latlog = obtener_latlog(ciudad)
    if latlog:
        lat = latlog["results"][0]["latitude"]
        lon = latlog["results"][0]["longitude"]
    datos = mostrar_datos_ciudad(lat,lon)
    print(f"Datos de {ciudad}")
    print(f"Temperatura : {datos["current_weather"]["temperature"]}°C")
    print(f"Velocidad del viento en : {datos["current_weather"]["windspeed"]}km/h")
    if datos["current_weather"]["weathercode"] == 0:
        print(f"Estado del clima : Despejado ")
    elif datos["current_weather"]["weathercode"] == 1:
        print("Estado del Clima : Mayormente despejado")
    elif datos["current_weather"]["weathercode"] == 2:
        print("Estado del Clima : Parcialmente nublado")
    elif datos["current_weather"]["weathercode"] == 3:
        print("Estado del Clima : Nublado")
    elif datos["current_weather"]["weathercode"] == 61:
        print("Estado del Clima : Lluvioso")
main()