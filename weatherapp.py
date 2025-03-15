import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "YOUR_API_KEY"  # Replace with your API key

def get_weather(city):
    """Fetches weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Could not fetch weather data: {e}")
        return None

def display_weather(weather_data):
    """Displays weather information in a GUI."""
    if weather_data:
        try:
            city = weather_data["name"]
            temperature = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            wind_speed = weather_data["wind"]["speed"]

            result_label.config(text=f"Weather in {city}:\n"
                                     f"Temperature: {temperature}°C\n"
                                     f"Description: {description}\n"
                                     f"Wind Speed: {wind_speed} m/s")
        except KeyError:
            messagebox.showerror("Error", "Invalid weather data received.")
    else:
        result_label.config(text="Weather data not available.")

def on_get_weather():
    """Handles the 'Get Weather' button click."""
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        display_weather(weather_data)
    else:
        messagebox.showerror("Error", "Please enter a city.")

# GUI setup
window = tk.Tk()
window.title("Weather App")

city_label = tk.Label(window, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text="Get Weather", command=on_get_weather)
get_weather_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()