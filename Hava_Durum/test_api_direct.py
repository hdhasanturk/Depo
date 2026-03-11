"""
Doğrudan API Anahtarı Test Scripti
API anahtarınızı doğrudan test eder ve sorunları gösterir.
"""

import requests

print("="*70)
print("🔍 DOĞRUDAN API ANAHTARI TEST")
print("="*70)

# API anahtarınızı buraya yapıştırın
api_key = input("\nAPI anahtarınızı buraya yapıştırın: ").strip()

if not api_key:
    print("❌ API anahtarı girilmedi!")
    exit()

# API anahtarını temizle
api_key = api_key.strip().strip('"').strip("'")

print(f"\n📋 API Anahtarı Bilgileri:")
print(f"   Uzunluk: {len(api_key)} karakter")
print(f"   İlk 8 karakter: {api_key[:8]}")
print(f"   Son 4 karakter: {api_key[-4:]}")
print(f"   Tam anahtar: {api_key}")

# Test isteği
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "London",
    "appid": api_key,
    "units": "metric"
}

print(f"\n🌐 Test isteği gönderiliyor...")
print(f"   URL: {url}")
print(f"   Şehir: London")
print(f"   API Key: {api_key[:8]}...{api_key[-4:]}")

try:
    response = requests.get(url, params=params, timeout=10)
    print(f"\n📊 HTTP Durum Kodu: {response.status_code}")
    
    veri = response.json()
    print(f"📊 API Yanıtı: {veri}")
    
    if "cod" in veri:
        kod = veri["cod"]
        if kod == 200:
            print(f"\n✅ BAŞARILI! API anahtarınız çalışıyor!")
            print(f"   Şehir: {veri.get('name', 'N/A')}")
            print(f"   Sıcaklık: {veri.get('main', {}).get('temp', 'N/A')}°C")
            print(f"\n💡 Bu API anahtarını new.env dosyasına şu şekilde yazın:")
            print(f"OPENWEATHER_API_KEY={api_key}")
        elif kod == 401:
            print(f"\n❌ HATA: Geçersiz API anahtarı (Kod: 401)")
            mesaj = veri.get("message", "Bilinmeyen hata")
            print(f"   Mesaj: {mesaj}")
            print(f"\n🔍 Olası Nedenler:")
            print(f"   1. API anahtarı henüz aktif olmamış (10 dakika - 2 saat bekleyin)")
            print(f"   2. API anahtarı yanlış kopyalanmış")
            print(f"   3. OpenWeatherMap hesabınızda sorun var")
            print(f"\n💡 Çözüm:")
            print(f"   - Birkaç saat bekleyip tekrar deneyin")
            print(f"   - OpenWeatherMap'ten yeni bir API anahtarı oluşturun")
            print(f"   - https://home.openweathermap.org/api_keys adresinden kontrol edin")
        else:
            print(f"\n⚠️  Beklenmeyen yanıt (Kod: {kod})")
            print(f"   Mesaj: {veri.get('message', 'Bilinmeyen hata')}")
    else:
        print(f"\n⚠️  Yanıt formatı beklenmedik")
        print(f"   Yanıt: {veri}")
        
except requests.exceptions.RequestException as e:
    print(f"\n❌ İstek hatası: {e}")
    print(f"   İnternet bağlantınızı kontrol edin")

print("\n" + "="*70)

