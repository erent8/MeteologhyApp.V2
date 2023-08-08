# MeteologhyApp.V2 
###### API almak için https://openweathermap.org/api sitesine girerek kayıt oluyoruz. ardından almak istediğimiz veriye göre API seçiyoruz ve projemize entegre ediyoruz...


1. İlk olarak, gerekli kütüphaneleri içe aktarıyoruz: requests ile HTTP istekleri yapmak ve datetime ile zaman işlemleri yapmak için kuruyoruz...
```
import requests
import datetime
```
2. OpenWeatherMap API anahtarını ve temel URL'sini tanımlıyoruz(Site üzerinden API anahtarı almanız gerekmektedir...)
```
API_KEY = "823bcb1f8964ccdb90c1fe8103fb981b"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
```
3. Kullanıcıdan şehir ismi alarak API isteği için tam URL'yi oluşturuyoruz:
```
SEHIR_ISMI = input("Şehir ismi giriniz...")
URL = BASE_URL + "appid=" + API_KEY + "&q=" + SEHIR_ISMI
```
4. API'ye istek atarak hava durumu verilerini alıyoruz ve JSON formatına çeviriyoruz:
```
gelen_veri = requests.get(URL) 
gelen_veri_JSON = gelen_veri.json()
```
5. yon_donus adlı bir fonksiyon tanımlıyoruz, bu fonksiyon verilen rüzgar yönünü derece cinsinden alır ve daha anlaşılır bir yön adı ile döner.

6. API yanıtında 'cod' anahtarının 404 olmadığını kontrol ederek veri alımını doğruluyoruz:
```
if gelen_veri_JSON['cod'] != "404":
```
7. Hava durumu tahminlerini içeren forecasts listesini alıyoruz:
```
forecasts = gelen_veri_JSON["list"]
```
Her bir tahmin verisi için aşağıdaki adımları gerçekleştiriyoruz:


8. Unix zaman damgasını alıyoruz:
```
timestamp = forecast["dt"]
```

9. Sıcaklık değerlerini alıyoruz:
```
temp_kelvin = forecast["main"]["temp"]
temp_min = forecast["main"]["temp_min"]
temp_max = forecast["main"]["temp_max"]
```
10. Diğer hava durumu verilerini alıyoruz:
```
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
```
11. Unix zaman damgasını datetime nesnesine çeviriyoruz:
```
tarih = datetime.datetime.fromtimestamp(timestamp)
```
12. Sıcaklık değerlerini Kelvin'den Celsius'a dönüştürüyoruz:
```
temp_celsius = temp_kelvin - 273.15
temp_celsius_min = temp_min - 273.15
temp_celsius_max = temp_max - 273.15
```
13. Rüzgar yönünü daha anlaşılır bir biçimde ifade etmek için yon_donus fonksiyonunu kullanıyoruz:
 ```
ruzgar_yonu = yon_donus(wind_direction)
```
14. Aldıgımız verileri ekrana yazdırıyoruz:
 ```
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
```
15. Eğer şehir adı geçerli değilse (404 hatası alınırsa) kullanıcıya bir hata mesajı gösteriyoruz:
 ```
else:
    print("Geçersiz şehir adı...")
```


#### Aldığımız çıktılar...
5 gün içerisinde 3 saatlik tahminler sunmaktadır.
![Ekran görüntüsü 2023-08-08 164411](https://github.com/erent8/MeteologhyApp.V2/assets/86615310/6b090f7a-5a24-449c-a5b0-a5631a70e5a0)
------------------------------------------------
![day1](https://github.com/erent8/MeteologhyApp.V2/assets/86615310/b65048e0-6b38-4c2c-be56-8176148f135a)
------------------------------------------------









    















