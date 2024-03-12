from dotenv import load_dotenv
import requests
import os
import json

load_dotenv() 



key = os.getenv("API_KEY")

def city_to_coordinates(city,country=None):
    try:
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={key}")
        result = json.loads(response.text)
        coordinates = [result[0]['lat'], result[0]['lon']]
        return coordinates
    except (IndexError, KeyError):
        return None
def zipcode_to_coordinates(zipcode):
    try:
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode}&appid={key}")
        result = json.loads(response.text)
        coordinates = [result['lat'], result['lon']]
        return coordinates
    except (IndexError, KeyError):
        return None
def get_weather_data(coordinates):
    if coordinates == None:
        return ["Invalid input!"]
    lat = coordinates[0]
    lon = coordinates[1]
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={key}")
    result = json.loads(response.text)
    weather_type = f"Weather: {result['weather'][0]['main']} - {result['weather'][0]['description']}"
    temperature = f"Temperature: {result['main']['temp']}"
    feels_like = f"Feels Like: {result['main']['feels_like']}"
    low_temp = f"Low: {result['main']['temp_min']}"
    high_temp = f"High: {result['main']['temp_max']}"
    
    return [weather_type,temperature,feels_like,low_temp,high_temp]

# coordinates = city_to_coordinates('fadsgag')
# print(get_weather_data(coordinates))