import requests

def get_weather(city_name, api_key):
    """
    Obtiene los datos del clima para una ciudad específica usando la API de OpenWeatherMap.
    
    :param city_name: Nombre de la ciudad.
    :param api_key: Tu clave de API de OpenWeatherMap.
    :return: Diccionario con los datos del clima o un mensaje de error.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",  # Para obtener la temperatura en grados Celsius
        "lang": "es"        # Idioma español
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    # Reemplaza 'TU_API_KEY' con tu clave de API de OpenWeatherMap
    api_key = "TU_API_KEY"
    city_name = input("Introduce el nombre de la ciudad: ")
    
    weather_data = get_weather(city_name, api_key)
    
    if "error" in weather_data:
        print(f"Error al obtener los datos del clima: {weather_data['error']}")
    else:
        print(f"Clima en {weather_data['name']}:")
        print(f"Temperatura: {weather_data['main']['temp']}°C")
        print(f"Descripción: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Humedad: {weather_data['main']['humidity']}%")
        print(f"Velocidad del viento: {weather_data['wind']['speed']} m/s")

if __name__ == "__main__":
    main()