import requests


def get_weather(city):
    api_key = "22823e5282524fc6d09b290e710c64b6"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            print(f"temperature: {temp}°C")
            print(f"condition: {condition}")
            print(f"humidity: {humidity}%")

        else:
            print("City not found. Please check the city name and try again.")
    
    except Exception as e:
        print("Error", e)

city = input("Enter city name: ").strip()
if city:
    get_weather(city)

else:
    print("Enter a valid city name.")