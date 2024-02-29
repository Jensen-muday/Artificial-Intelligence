# programmer: Jensen Muday
# Date: 2.29.2024
# program: AI Playground
# Zip Code: 49083
import requests
# pip install requests


print("this will be a place for me to play with programming using AI Technology\n")


def get_weather(zip_code, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return city, weather_description, temperature, humidity, wind_speed
    else:
        print("Error:", response.status_code)
        return None


def main():
    zip_code = input("Enter your ZIP code: ")
    api_key = "c396df4676ac8eaded4c63497d34476f"  # Replace with your actual API key from OpenWeatherMap
    city, description, temperature, humidity, wind_speed = get_weather(zip_code, api_key)
    if city:
        print(f"Weather in {city}:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    main()
