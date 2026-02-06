from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def build_weather_url(city, units):
    """
    Build and return the OpenWeather API URL.
    
    :param city: City name (string)
    :param units: 'metric' or 'imperial'
    :return: Complete API URL (string)
    """
    return (
        f"{BASE_URL}?q={city}&units={units}&appid={API_KEY}"
    )
