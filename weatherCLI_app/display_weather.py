def display_weather(data):
    if not data or data.get("temperature") is None:
        print("Temperature data unavailable.")
        return
    
    units = data.get("units", "metric")
    unit_symbol = "°F" if units == "imperial" else "°C"

    city = data.get("city", "Unknown")
    country = data.get("country")
    location = f"{city}, {country}" if country else city

    wind_deg = data.get("wind_deg")
    wind_dir = data.get("wind_dir")

    if wind_deg is not None and wind_dir is not None:
        wind_direction_str = f"{wind_deg}° ({wind_dir})"
    else:
        wind_direction_str = "Not available"

    last_updated = data.get("last_updated")
    if last_updated:
        time_str=f"{last_updated.strftime('%d %b %Y, %I:%M %p UTC')}"

    print(
        f"Weather in {location}:\n"
        f"temperature: {data.get('temperature')}{unit_symbol},\n" 
        f"feels like: {data.get('feels_like')}{unit_symbol},\n"
        f"description: {data.get('description')},\n" 
        f"humidity: {data.get('humidity')}%,\n"
        f"wind speed: {data.get('wind_speed')},\n"
        f"pressure: {data.get('pressure')},\n"
        f"wind direction: {wind_direction_str},\n"
        f"Last updated: {time_str}"
    )
