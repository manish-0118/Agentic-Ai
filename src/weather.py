import os
import requests
# from dotenv import load_dotenv

API_KEY=os.getenv("WEATHER_API_KEY", "")
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def get_coordinates(city):
    response=requests.get(GEOCODE_URL, params={"name": city, "count":1}, timeout=10)
    return response.json()
data=get_coordinates("kathmandu")
# print(data)
lat=data["results"][0]["latitude"]
lon=data["results"][0]["longitude"]
    
def get_weather(lati,longi):
    response=requests.get(FORECAST_URL,params={"latitude":lati, "longitude":longi,"current":"temperature_2m,relative_humidity_2m,wind_speed_10m"}, timeout=10)
    return response.json()
data2=get_weather(lat,lon)
print(f"Temperature:{data2['current']['temperature_2m']}°C")