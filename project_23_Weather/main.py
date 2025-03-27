import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API key not found. Please set it in the .env file.")
    exit()

city = input("Enter city name: ").strip()

if not city:
    print("Error: City name cannot be empty.")
    exit()

base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(base_url)
    response.raise_for_status()  

    weather_data = response.json()

    if weather_data.get("cod") != 200:
        print(f"Error: {weather_data.get('message', 'Unable to fetch weather data')}.")
        exit()

    city_name = weather_data.get("name", "N/A")
    country = weather_data.get("sys", {}).get("country", "N/A")
    temperature = weather_data.get("main", {}).get("temp", "N/A")
    feels_like = weather_data.get("main", {}).get("feels_like", "N/A")
    humidity = weather_data.get("main", {}).get("humidity", "N/A")
    weather_description = weather_data.get("weather", [{}])[0].get("description", "N/A")
    wind_speed = weather_data.get("wind", {}).get("speed", "N/A")
    visibility = weather_data.get("visibility", "N/A")

    print("\nWeather Report:")
    print(f"City: {city_name}, {country}")
    print(f"Temperature: {temperature} °C (Feels like: {feels_like} °C)")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Visibility: {visibility} meters")

except requests.exceptions.RequestException as e:
    print(f"Error: Unable to connect to the weather service. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")