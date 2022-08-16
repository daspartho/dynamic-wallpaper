import geocoder
import requests
import os
from dotenv import load_dotenv
import random
import platform
import time

load_dotenv() # loads environment variables

def get_lat_lon():
    g = geocoder.ip('me')
    return g.latlng # returns user coordinates

def get_weather(lat, lon):
    '''takes coordinates as argument and returns weather description at that location'''
    key = os.getenv("WEATHER_API_KEY")
    payload = {'lat':lat, 'lon':lon, 'appid':key}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    data = response.json()
    return data["weather"][0]["main"] # returns weather description

def get_wallpaper(weather_desc):
    '''Downloads a wallpaper based on weather description and returns path to it'''
    ID = os.getenv("UNSPLASH_CLIENT_ID")
    payload = {'query':f'{weather_desc} wallpaper', 'client_id':ID, 'per_page':30 ,'orientation':'landscape'}
    response = requests.get('https://api.unsplash.com/search/photos', params=payload)
    data = response.json()
    img_url = data['results'][random.randint(0,29)]['links']['download'] # selects a random image from the first 30 images in the search results
    img_data = requests.get(img_url).content
    img_path = os.path.expanduser('~/wallpaper.jpg') # path for saving the wallpaper
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
    return img_path # return path for the downloaded image

def set_wallpaper(img_path):
    '''Takes an image path as argument and sets it as wallpaper'''

    if platform.system()=='Linux': # for Linux systems
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file:{img_path}")
    
    elif platform.system()=='Windows': # for Windows systems
        import ctypes
        ctypes.windll.user32.SystemParametersInfoA(20,0,img_path, 0)
    
    elif platform.system()=='Darwin': # for MacOS systems
        os.system(f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file {img_path}'")

def main():
    lat, lon = get_lat_lon() # coordinates
    weather_desc = get_weather(lat, lon) # weather description
    img_path = get_wallpaper(weather_desc) # path to downloaded wallpaper
    set_wallpaper(img_path) # sets as wallpaper

if __name__=="__main__":
    while True:
        main()
        time.sleep(300) # loops every 5 minutes