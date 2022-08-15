import geocoder
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_lat_lon():
    g = geocoder.ip('me')
    return g.latlng

def get_weather(lat, lon):
    key = os.getenv("WEATHER_API_KEY")
    payload = {'lat':lat, 'lon':lon, 'appid':key}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    data = response.json()
    return data["weather"][0]["main"]