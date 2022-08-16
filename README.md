# Dynamic Wallpaper

Dynamic Wallpaper automatically changes your desktop wallpaper based on your weather!

# How it works

Dynamic Wallpaper fetches weather condition details using OpenWeatherMap API.

Then searches for wallpaper images related to the weather condition through Unsplash API, downloads an image and applies it as wallpaper.

It checks for weather updates every 5 minutes.

# Requirements
- Python 3
- Pip (Python's Package Manager)

# Installation
- First, clone the repository.
```
git clone https://github.com/daspartho/dynamic-wallpaper.git 
```
- Then, change your current directory into the dynamic-wallpaper repository.
```
cd dynamic-wallpaper
```
- Finally, install the requirements in the requirements file.
```
pip install -r requirements.txt
```
- From here, dynamic-wallpaper is installed. Continue to the Setting Up section in order to connect dynamic-wallpaper to the APIs.

# Setting up

You need to do these only the first time.

- Create a `.env` file.
- OpenWeatherMap API setup
    1. Go to https://home.openweathermap.org/users/sign_up and sign up.
    2. Now on the dashboard click on API keys option and copy the key given.
    3. Go to the `.env` file and paste the key like this `WEATHER_API_KEY=<your-key>`
- Unsplash API setup
    1. Go to https://unsplash.com/join and sign up. Then go to Application dashboard from here https://unsplash.com/oauth/applications.
    2. Now on the dashboard click on 'New Application', accept the terms, fill in a cool name and description for the application (it doesn't matter what you put) and create an application.
    3. Then go to the keys section on the application dashboard and copy the Access Key (no need for secret key).
    4. Go to the `.env` file and paste the key like this
    `UNSPLASH_CLIENT_ID=<your-key>`
- ⚠️ **Please remember to never share your keys with anyone.**

# Usage
Run the script from a terminal using `python main.py` in the local repository's directory (or probably by double-cliking on the `main` python script from your file explorer on Windows).

Congratulations! You will now have beautiful wallpapers that changes according to weather.

# Contributing
If you want to contribute code, just write a quick pull request and the developers will take a look at it.
If you want to suggest an idea, just write an issue and the developers will check it out!
