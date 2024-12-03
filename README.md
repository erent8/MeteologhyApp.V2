# MeteorologyAppV2 
--------------------------------------------------------------------------------------------------------------------------------


###### To get the API https://openweathermap.org/api we register by entering the website. then we select the API according to the data we want to get and integrate it into our project...


1. First, we import the necessary libraries: we install them to make HTTP requests with requests and time transactions with datetime...
`'python
import requests
import datetime
```
2. We define the OpenWeatherMap API key and its basic URL(You need to get the API key through the Site...)
`'python
API_KEY = "YOUR_API_KEY"
BASE_URL="http://api.openweathermap.org/data/2.5/forecast ?"
```
3. We create the full URL for the API request by taking the city name from the user:
`'python
SEHIR_ISMI = input("Enter the city name...")
URL=BASE_URL+"appid="+API_KEY+"&q="+CITY_ISMI
```
4. We take the weather data by sending a request to the API and convert it to JSON format:
`'python
in_veri = requests.get(URL) 
INEN_VERI_JSON = inen_veri.json()
```
5. we define a function called yon_donus, this function takes the given wind direction in degrees and returns with a more understandable direction name.


6. We verify the data reception by checking that the 'cod' key in the API response is not 404:
`'python
if from_veri_json['cod'] != "404":
```
7. We get the list of forecasts containing weather forecasts:
`'python
forecasts = IN_VERI_JSON["list"]
```
We perform the following steps for each forecast data:


8. We get the Unix timestamp:
`'python
timestamp = forecast["dt"]
```

9. We take the temperature values:
`'python
temp_kelvin = forecast["main"]["temp"]
temp_min = forecast["main"]["temp_min"]
temp_max = forecast["main"]["temp_max"]
```
10. We receive other weather data:
`'python
humidity = forecast["main"]["humidity"]
wind_speed = forecast["wind"]["speed"]
wind_direction = forecast["wind"]["deg"]
clouds = forecast["clouds"]["all"]
rain = forecast.get("rain", {}).get("3h", 0)
snow = forecast.get("snow", {}).get("3h", 0)
visibility = forecast["visibility"]
uv_index = forecast.get("uv", 0)
description = forecast["weather"][0]["description"]
pressure = forecast["main"]["pressure"]
country = from_veri_json["city"]["country"]
```
11. We are converting the Unix timestamp to a datetime object:
`'python
date = datetime.datetime.fromtimestamp(timestamp)
```
12. We convert the temperature values from Kelvin to Celsius:
`'python
temp_celsius = temp_kelvin - 273.15
temp_celsius_min= temp_min - 273.15
temp_celsius_max = temp_max - 273.15
```
13. We use the yon_donus function to express the wind direction more clearly:
 `'python
wind_ion= wind_donus(wind_direction)
```
14. We print the data we receive on the screen:
 `'python
print("Date and Time:", date_str)
print("Day:", gun)
print("Temperature: {:.2f} °C".format(temp_celsius))
print("Lowest Temperature: {:.2f} °C".format(temp_celsius_min))
print("Highest Temperature: {:.2f} °C".format(temp_celsius_max))
print("Humidity:", humidity, "%")
print("Wind Speed:", wind_speed, "m/s")
print("Wind Direction:", wind direction)
print("Cloud Ratio:", clouds, "%")
print("Precipitation (3 Hours):", rain, "mm")
print("Snow (3 Hours):", snow, "mm")
print("Viewing Distance:", visibility, "meter")
print("UV Index:", uv_index)
print("Weather:", description)
print("Pressure:", pressure, "hPa")
print("Country:", country)
print("------------------------")
```
15. If the city name is not valid (if a 404 error is received), we show an error message to the user:
 `'python
else:
    print("Invalid city name...")
```


#### The printouts we bought...

![Figure_1](https://github.com/erent8/MeteorolojiAppV2/assets/86615310/79905002-07ed-4879-b840-37531bae7110)



it offers forecasts at 5-day December and 3-hour intervals.
------------------------------------------------

![Screenshot 2023-08-08 164411](https://github.com/erent8/MeteologhyApp.V2/assets/86615310/6b090f7a-5a24-449c-a5b0-a5631a70e5a0)
------------------------------------------------
![day1](https://github.com/erent8/MeteologhyApp.V2/assets/86615310/b65048e0-6b38-4c2c-be56-8176148f135a)
------------------------------------------------
