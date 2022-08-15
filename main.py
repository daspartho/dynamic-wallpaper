import geocoder
import requests
import os
from dotenv import load_dotenv
import random

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

def get_wallpaper(weather_desc):
    ID = os.getenv("UNSPLASH_CLIENT_ID")
    payload = {'query':f'{weather_desc} wallpaper', 'client_id':ID, 'per_page':30 ,'orientation':'landscape'}
    response = requests.get('https://api.unsplash.com/search/photos', params=payload)
    data = response.json()
    img_url = data['results'][random.randint(0,29)]['links']['download']
    img_data = requests.get(img_url).content
    with open('wallpaper.jpg', 'wb') as handler:
        handler.write(img_data)