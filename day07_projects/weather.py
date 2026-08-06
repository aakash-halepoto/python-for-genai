import requests

# 1. get_weather(latitude, longitude) — the fetcher:
# Sends a GET to this URL (build it with an f-string, plugging in the coordinates):
#   https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true
# Guard on status: if 200, return response.json(); else return None

def get_weather(latitude,longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
    if response.status_code ==  200:
        data = response.json()
        return data
    else:
        return None
        


# 2. show_weather(city_name, latitude, longitude) — the display:

# Calls get_weather(...)
# If it returned None → print "Could not fetch weather for {city_name}" and return (guard clause)
# Otherwise, peel into the response: current weather lives at data["current_weather"], which contains temperature and windspeed
# Print: "{city_name}: {temp}°C, wind {wind} km/h"

def show_weather(city_name,latitude,longitude):
    weather_data = get_weather(latitude,longitude)
    if weather_data is None:
        print(f"Could not fetch weather for {city_name}")
        return
    current = weather_data['current_weather']
    print(f"{city_name}: {current['temperature']}°C, wind {current['windspeed']} km/h")

# Test


show_weather("Hyderabad", 25.39, 68.37)
show_weather("Karachi", 24.86, 67.00)
show_weather("Islamabad", 33.68, 73.04)