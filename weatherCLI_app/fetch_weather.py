import requests
from config import API_KEY
from url_builder import build_weather_url
from datetime import datetime
def fetch_weather():
    city_name=get_city_name()
    units = get_units_from_user()

    url = build_weather_url(city_name, units)

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out. The server is taking too long to respond.")
        return None
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        display_error(status_code) 
        return None
    #     if response.status_code == 404:
    #         print("City not found. Please check the spelling.")
    #     elif response.status_code == 401:
    #         print("Invalid API key.")
    #     else:
    #         print(f"HTTP error: {response.status_code}")
    except ValueError:
        print("Error parsing weather data.")
        return None
    
    # print(json.dumps(data, indent=2))
    city = data.get("name", "Unknown location")
    
    main = data.get("main", {})
    wind = data.get("wind", {})
    clouds = data.get("clouds", {})
    sys = data.get("sys", {})
    dt = data.get("dt")
    
    country = sys.get("country")
    temperature = main.get("temp")
    pressure = main.get("pressure")
    wind_deg=wind.get("deg")
    wind_speed = wind.get("speed")
    cloudiness = clouds.get("all")
    feelslike_temp = main.get("feels_like")
    humidity = main.get("humidity")
    weather_list = data.get("weather", [])
    weather_description = "No description available"
    if weather_list:
        weather_description = weather_list[0].get("description", weather_description)
    wind_dir = deg_to_direction(wind_deg)
    last_updated = datetime.utcfromtimestamp(dt) if dt else None
   
    return {
    "city": city,
    "country": country,
    "temperature": temperature,
    "feels_like": feelslike_temp,
    "pressure": pressure,
    "wind_speed": wind_speed,
    "cloudiness": cloudiness,
    "humidity": humidity,
    "description": weather_description,
    "units":units,
    "wind_dir":wind_dir,
    "wind_deg":wind_deg,
    "last_updated": last_updated
}
        
def get_units_from_user():
    while True:
        choice = input("Choose units (C for Celsius, F for Fahrenheit) [C/F]: ").strip().upper()

        if choice == "C":
            return "metric"
        elif choice == "F":
            return "imperial"
        else:
            print("Invalid choice. Please enter C or F.")

def get_city_name():
    while True:
        city_name = input("Enter city: ").strip()

        if not city_name:
            print("City name cannot be empty.")
            continue
        return city_name

def display_error(status_code):
    if status_code == 400:
        print("400 Bad Request: The server could not understand the request.")
    elif status_code == 401:
        print("401 Unauthorized: Authentication is required.")
    elif status_code == 403:
        print("403 Forbidden: You do not have permission to access this resource.")
    elif status_code == 404:
        print("404 Not Found: The requested resource was not found. Please check the spelling")
    elif status_code == 429:
        print("429 Too Many Requests: You are being rate limited.")
    elif status_code == 500:
        print("500 Internal Server Error: Something went wrong on the server.")
    elif status_code == 503:
        print("503 Service Unavailable: Server is temporarily unavailable.")
    else:
        print(f"{status_code} Unknown Error: An unexpected error occurred.")

def deg_to_direction(deg):
    if deg is None:
        return None
    directions = [
        "N", "NE", "E", "SE",
        "S", "SW", "W", "NW"
    ]
    index = round(deg / 45) % 8
    return directions[index]

