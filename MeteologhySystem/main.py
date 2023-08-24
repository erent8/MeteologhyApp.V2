import requests
import datetime

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"

SEHIR_ISMI = input("Şehir ismi giriniz...")

URL = BASE_URL + "appid=" + API_KEY + "&q=" + SEHIR_ISMI

gelen_veri = requests.get(URL)
gelen_veri_JSON = gelen_veri.json()

def yon_donus(yon):
    if 337.5 <= yon < 22.5:
        return "Kuzey"
    elif 22.5 <= yon < 67.5:
        return "Kuzeydoğu"
    elif 67.5 <= yon < 112.5:
        return "Doğu"
    elif 112.5 <= yon < 157.5:
        return "Güneydoğu"
    elif 157.5 <= yon < 202.5:
        return "Güney"
    elif 202.5 <= yon < 247.5:
        return "Güneybatı"
    elif 247.5 <= yon < 292.5:
        return "Batı"
    else:
        return "Kuzeybatı"

if gelen_veri_JSON['cod'] != "404":
    forecasts = gelen_veri_JSON["list"]  # Hava durumu tahminlerini içeren liste

    for forecast in forecasts:
        timestamp = forecast["dt"]  # Unix zaman damgası
        temp_kelvin = forecast["main"]["temp"]
        temp_min = forecast["main"]["temp_min"]
        temp_max = forecast["main"]["temp_max"]
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
        country = gelen_veri_JSON["city"]["country"]

        tarih = datetime.datetime.fromtimestamp(timestamp)
        gun = tarih.strftime("%A")
        tarih_str = tarih.strftime("%d/%m/%Y %H:%M")

        temp_celsius = temp_kelvin - 273.15
        temp_celsius_min = temp_min - 273.15
        temp_celsius_max = temp_max - 273.15

        ruzgar_yonu = yon_donus(wind_direction)

        print("Tarih ve Saat:", tarih_str)
        print("Gün:", gun)
        print("Sıcaklık: {:.2f} °C".format(temp_celsius))
        print("En Düşük Sıcaklık: {:.2f} °C".format(temp_celsius_min))
        print("En Yüksek Sıcaklık: {:.2f} °C".format(temp_celsius_max))
        print("Nem Oranı:", humidity, "%")
        print("Rüzgar Hızı:", wind_speed, "m/s")
        print("Rüzgar Yönü:", ruzgar_yonu)
        print("Bulut Oranı:", clouds, "%")
        print("Yağış (3 Saatlik):", rain, "mm")
        print("Kar (3 Saatlik):", snow, "mm")
        print("Görüş Uzaklığı:", visibility, "metre")
        print("UV İndeksi:", uv_index)
        print("Hava Durumu:", description)
        print("Basınç:", pressure, "hPa")
        print("Ülke:", country)
        print("------------------------")

else:
    print("Geçersiz şehir adı...")
