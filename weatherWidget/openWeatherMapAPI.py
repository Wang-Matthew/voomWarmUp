# some code from https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
from ast import Return
import requests
import json
import time
from datetime import datetime

# Enter your API key here
api_key = "75ac6a16b870a9dff9cb29020876dcd0"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# function to call from hell


def return_weather(city_name):
    start_time = time.perf_counter()
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # wind speed
        current_wind = x["wind"]["speed"]

        # weather icon
        current_icon = x["weather"][0]["icon"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        request_time = time.perf_counter() - start_time

        # return array of weather info in this order: [city name, temp in fahrenheit, wind speed, humdity in percentage, weather description,  weather icon, response time, query time]

        return([city_name, str(round((1.8 * (current_temperature - 273) + 32), 2)), str(current_wind),
               str(current_humidity), str(
                   weather_description), "https://openweathermap.org/img/wn/" + str(current_icon) + ".png",
                str(round(request_time, 3)), datetime.now().strftime("%d/%m/%Y %H:%M:%S")])

    else:
        return([" City Not Found "])
