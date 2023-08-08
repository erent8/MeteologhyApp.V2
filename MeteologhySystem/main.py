import requests

API_KEY = "823bcb1f8964ccdb90c1fe8103fb981b"
BASE_URL = "http://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid={823bcb1f8964ccdb90c1fe8103fb981b}"

SEHIR_ISMI = input("Şehir ismi giriniz...")

URL = BASE_URL + "appid=" + API_KEY + "&q=" + SEHIR_ISMI

gelen_veri = requests.get(URL)
gelen_veri_JSON = gelen_veri.json()

if gelen_veri_JSON['cod'] != "404":
    temp_kelvin = gelen_veri_JSON["main"]["temp"]
    description = gelen_veri_JSON["weather"][0]["description"]
    pressure = gelen_veri_JSON["main"]["pressure"]
    country = gelen_veri_JSON["sys"]["country"]

    # Kelvin'i Celsius'a dönüştürme: °C = K - 273.15
    temp_celsius = temp_kelvin - 273.15

    print("Sıcaklık: {:.2f} °C".format(temp_celsius))
    print("Hava Durumu:", description)
    print("Basınç:", pressure, "hPa")
    print("Ülke:", country)

else:
    print("Geçersiz şehir adı...")
