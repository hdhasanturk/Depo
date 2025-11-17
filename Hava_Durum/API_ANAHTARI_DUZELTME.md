# 🔧 API Anahtarı 401 Hatası Çözüm Rehberi

## ❌ Hata: "Invalid API key" (Kod: 401)

Bu hata, OpenWeatherMap API'nin API anahtarınızı tanımadığı anlamına gelir.

## 🔍 Adım Adım Çözüm

### 1️⃣ OpenWeatherMap Hesabınızı Kontrol Edin

1. **OpenWeatherMap sitesine giriş yapın:**
   - https://openweathermap.org/ adresine gidin
   - Sağ üst köşeden "Sign In" butonuna tıklayın
   - Hesabınıza giriş yapın

2. **API Keys sayfasına gidin:**
   - Sağ üst köşedeki kullanıcı adınıza tıklayın
   - "My API keys" seçeneğine tıklayın
   - Veya doğrudan: https://home.openweathermap.org/api_keys

### 2️⃣ API Anahtarınızı Kontrol Edin

**Mevcut API anahtarınızı kontrol edin:**
- API anahtarınız listede görünüyor mu?
- Durumu "Active" mi?
- Eğer "Inactive" ise, aktifleştirmeniz gerekebilir

### 3️⃣ Yeni API Anahtarı Oluşturun (Önerilen)

Eğer mevcut API anahtarı çalışmıyorsa, yeni bir tane oluşturun:

1. **"Create key" butonuna tıklayın**
2. **Key name girin:** (örn: "Hava Durumu Uygulaması")
3. **"Generate" butonuna tıklayın**
4. **⚠️ ÖNEMLİ:** API anahtarınızı hemen kopyalayın! (bir daha gösterilmeyebilir)

### 4️⃣ API Anahtarını .env Dosyasına Ekleyin

1. **`new.env` dosyasını açın** (veya `.env` oluşturun)
2. **İçine şunu yazın:**
   ```
   OPENWEATHER_API_KEY=buraya_yeni_api_anahtarinizi_yazin
   ```
   - Eşittir işaretinden sonra boşluk OLMAMALI
   - Tırnak işareti OLMAMALI
   - Satır sonunda boşluk OLMAMALI

3. **Dosyayı kaydedin**

### 5️⃣ API Anahtarının Aktif Olmasını Bekleyin

⚠️ **ÖNEMLİ:** Yeni oluşturulan API anahtarları genellikle **10 dakika - 2 saat** arasında aktif hale gelir.

- İlk kullanımda hata alırsanız, bir süre bekleyip tekrar deneyin
- Bu normal bir durumdur

### 6️⃣ Test Edin

```bash
python api_test.py
```

veya

```bash
python Hava_durumu.py
```

## 🔍 API Anahtarı Formatı

Doğru format:
```
OPENWEATHER_API_KEY=520d1eb3eb389cb2014545f47f3f302fc
```

Yanlış formatlar:
```
OPENWEATHER_API_KEY= 520d1eb3eb389cb2014545f47f3f302fc  (boşluk var)
OPENWEATHER_API_KEY="520d1eb3eb389cb2014545f47f3f302fc" (tırnak var)
OPENWEATHER_API_KEY = 520d1eb3eb389cb2014545f47f3f302fc (eşittir etrafında boşluk)
```

## ❓ Sık Sorulan Sorular

### API anahtarım neden çalışmıyor?

1. **Yeni oluşturulduysa:** 10 dakika - 2 saat bekleyin
2. **Eski anahtarsa:** Yeni bir tane oluşturun
3. **Format hatası:** .env dosyasında boşluk veya tırnak olmamalı

### API anahtarımı nereden bulabilirim?

https://home.openweathermap.org/api_keys adresinden API anahtarlarınızı görebilirsiniz.

### Birden fazla API anahtarı oluşturabilir miyim?

Evet, ücretsiz planınızda birden fazla API anahtarı oluşturabilirsiniz.

## 🆘 Hala Çalışmıyorsa

1. OpenWeatherMap hesabınızın aktif olduğundan emin olun
2. E-posta doğrulamanızı tamamladığınızdan emin olun
3. Yeni bir hesap oluşturmayı deneyin
4. OpenWeatherMap destek ekibiyle iletişime geçin

