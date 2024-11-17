
import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        print(json_response["value"])
    else:
        print("Try again")

except requests.exceptions.RequestException:
    print("Request could not be completed.")


## exercise 2 weather

api = '3d71e969d1f18c751d6a62fee47103c7'
weather_url = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api}'
lat = 60.1699
lon = 24.9384 # should be replaced by selected result from database


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"

    try:
        response = requests.get(request_url)
        # response.raise_for_status()
        if response.status_code == 200:
            # test how it looks like
            # print(response.json())
            weather = response.json()
            print(type(weather))
            current_temp_kelvin = weather["main"]["temp"]
            temp_celsius = kelvin_to_celsius(current_temp_kelvin)

            print(f"{city}'s temperature：{round(temp_celsius)}°C")
        else:
            print("Try again")
    except requests.exceptions.RequestException:
        print("Request could not be completed.")


city_name = input("Enter city name: ")
get_weather(city_name)




