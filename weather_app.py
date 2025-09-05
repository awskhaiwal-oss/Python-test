import requests

# Add your own OpenWeatherMap API key
API_KEY = "85c517cc27a6afde96b5424ab89971a0"


def fetch_weather(city_name):
    """Fetch weather data for a given city."""
    # Construct the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    # Sending request
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        return response.json()
    else:
        return None


def print_weather_report(city_name, weather_json):
    """Print the weather report for a given city."""
    print("\n Weather Report for:", city_name)
    print("Temperature:", weather_json["main"]["temp"], "°C")
    print("Description:", weather_json["weather"][0]["description"])
    print("Humidity:", weather_json["main"]["humidity"], "%")


if __name__ == "__main__":
    # Ask the user for a city name
    city = input("Enter a city name: ")

    # Fetch weather data
    weather_data = fetch_weather(city)

    if weather_data:
        # Print the weather report
        print_weather_report(city, weather_data)
    else:
        print("Error: city not found.")
