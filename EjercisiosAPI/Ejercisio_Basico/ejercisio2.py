import requests

def obtener_datos(pais):
    url = f"https://restcountries.com/v3.1/name/{pais}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    pais_info = datos[0]
    
    # Extraer información
    capital = pais_info["capital"][0]
    poblacion = pais_info["population"]
    idioma = list(pais_info["languages"].values())[0]

    return capital, poblacion, idioma

def main():
    pais = input("Ingresa el nombre de un país: ")
    capital, poblacion, idioma = obtener_datos(pais)

    print(f"\nInformación del país '{pais}':")
    print(f"- Capital: {capital}")
    print(f"- Población: {poblacion}")
    print(f"- Idioma principal: {idioma}")
main()