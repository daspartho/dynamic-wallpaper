import geocoder
import requests
import os
from dotenv import load_dotenv
import random
import platform

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
    img_path = os.path.expanduser('~/wallpaper.jpg')
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
    return img_path

def set_wallpaper(img_path):
    if platform.system()=='Linux':
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file:{img_path}")
    elif platform.system()=='Windows':
        import ctypes
        ctypes.windll.user32.SystemParametersInfoA(20,0,img_path, 0)
    elif platform.system()=='Darwin':
        os.system(f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file {img_path}'")

def main():
    lat, lon = get_lat_lon()
    weather_desc = get_weather(lat, lon)
    img_path = get_wallpaper(weather_desc)
    set_wallpaper(img_path)

if __name__=="__main__":
    main()