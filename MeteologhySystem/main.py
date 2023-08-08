import requests
import datetime

API_KEY = "823bcb1f8964ccdb90c1fe8103fb981b"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"

SEHIR_ISMI = input("Şehir ismi giriniz...")

URL = BASE_URL + "appid=" + API_KEY + "&q=" + SEHIR_ISMI

gelen_veri = requests.get(URL)
gelen_veri_JSON = gelen_veri.json()

if gelen_veri_JSON['cod'] != "404":
    forecasts = gelen_veri_JSON["list"]  # Hava durumu tahminlerini içeren liste

    for forecast in forecasts:
        timestamp = forecast["dt"]  # Unix zaman damgası
        temp_kelvin = forecast["main"]["temp"]
        description = forecast["weather"][0]["description"]
        pressure = forecast["main"]["pressure"]
        country = gelen_veri_JSON["city"]["country"]

        # Unix zaman damgasını datetime nesnesine dönüştürme
        tarih = datetime.datetime.fromtimestamp(timestamp)
        gun = tarih.strftime("%A")  # Gün adını almak
        tarih_str = tarih.strftime("%d/%m/%Y %H:%M")  # Tarih ve saat bilgisini almak

        # Kelvin'i Celsius'a dönüştürme: °C = K - 273.15
        temp_celsius = temp_kelvin - 273.15

        print("Date Time:", tarih_str)
        print("Day:", gun)
        print("Temperature: {:.2f} °C".format(temp_celsius))
        print("Weather:", description)
        print("Pressure:", pressure, "hPa")
        print("Country:", country)
        print("------------------------")

else:
    print("Geçersiz şehir adı...")
