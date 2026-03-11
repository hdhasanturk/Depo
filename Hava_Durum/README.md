# 🌤️ Hava Durumu Uygulaması

OpenWeatherMap API kullanarak şehir bazlı güncel hava durumu bilgilerini gösteren basit Python uygulaması.

## 📋 Özellikler

- 🌍 Şehir bazlı hava durumu sorgulama
- 🌡️ Sıcaklık, nem, basınç, rüzgar hızı bilgileri
- 🌅 Gün doğumu ve gün batımı saatleri
- 🇹🇷 Türkçe dil desteği
- 🔄 Sürekli sorgulama imkanı

## 🚀 Kurulum

### 1. Gereksinimler

Python 3.6 veya üzeri sürüm gerekir.

### 2. Kütüphaneleri Yükle

```bash
pip install -r requirements.txt
```

### 3. API Anahtarı Alma

1. [OpenWeatherMap](https://openweathermap.org/api) sitesine gidin
2. Ücretsiz hesap oluşturun
3. API Keys bölümünden API anahtarınızı alın

### 4. API Anahtarını Ayarlama

**Yöntem 1: .env Dosyası (En Kolay - Önerilen)**

1. Proje klasöründe `.env` adında bir dosya oluşturun
2. İçine şunu yazın:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
3. Program otomatik olarak bu dosyayı okuyacaktır

**Yöntem 2: Ortam Değişkeni**

Windows PowerShell:
```powershell
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

Windows CMD:
```cmd
set OPENWEATHER_API_KEY=your_api_key_here
```

Linux/Mac:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

**Yöntem 3: Program İçinde**

Program çalıştırıldığında API anahtarı bulunamazsa, size soracaktır.

📖 **Detaylı rehber için:** `API_ANAHTARI_REHBERI.md` dosyasına bakın

## 💻 Kullanım

```bash
python Hava_durumu.py
```

Program çalıştıktan sonra:
1. Şehir adını girin (örn: Istanbul, Ankara, London)
2. Hava durumu bilgilerini görüntüleyin
3. Başka bir şehir sorgulamak için tekrar şehir adı girin
4. Çıkmak için 'q' tuşuna basın

## 📝 Örnek Kullanım

```
🌍 Şehir adını girin (çıkmak için 'q'): Istanbul

⏳ Istanbul için hava durumu bilgileri alınıyor...

==================================================
🌤️  HAVA DURUMU - ISTANBUL, TR
==================================================
📊 Durum: Açık
🌡️  Sıcaklık: 22.5°C
🤲 Hissedilen: 21.8°C
💧 Nem: %65
📉 Basınç: 1013 hPa
💨 Rüzgar Hızı: 3.2 m/s
🌅 Gün Doğumu: 06:15
🌇 Gün Batımı: 19:45
==================================================
```

## 🏗️ Proje Yapısı

```
Hava_Durum/
│
├── Hava_durumu.py           # Ana uygulama dosyası
├── requirements.txt         # Python bağımlılıkları
├── .env                     # API anahtarı (siz oluşturacaksınız)
├── .gitignore              # Git ignore dosyası
├── API_ANAHTARI_REHBERI.md # API anahtarı alma rehberi
└── README.md               # Proje dokümantasyonu
```

## 🔧 Geliştirme Notları

Bu proje öğrenme ve CV'ye katkı amaçlı basit bir başlangıç projesidir. İleride şu özellikler eklenebilir:

- 📊 Grafik ve görselleştirmeler
- 📱 GUI arayüzü (Tkinter, PyQt)
- 🌐 Web uygulaması (Flask/Django)
- 📅 Hava durumu tahminleri (5 günlük)
- 💾 Veritabanı entegrasyonu
- 📍 Konum bazlı otomatik sorgulama
- 🔔 Hava durumu bildirimleri

## 📚 Öğrenilen Konseptler

- RESTful API kullanımı
- HTTP istekleri (requests kütüphanesi)
- JSON veri işleme
- Hata yönetimi (exception handling)
- Ortam değişkenleri kullanımı
- OOP (Nesne Yönelimli Programlama) temelleri
- Kullanıcı arayüzü tasarımı

## 📄 Lisans

Bu proje eğitim amaçlıdır.

## 👤 Yazar

Hava Durumu Uygulaması - Öğrenme Projesi


