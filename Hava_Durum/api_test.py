"""
API Anahtarı Test Scripti
API anahtarınızın çalışıp çalışmadığını test eder.
"""

import requests
import os

# .env dosyasını yükle
try:
    from dotenv import load_dotenv
    if not load_dotenv('.env'):
        load_dotenv('new.env')
except ImportError:
    pass

def test_api_key(api_key):
    """API anahtarını test eder"""
    print("="*60)
    print("🔍 API ANAHTARI TEST EDİLİYOR")
    print("="*60)
    
    # API anahtarını temizle
    api_key = api_key.strip()
    
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
    
    try:
        response = requests.get(url, params=params, timeout=10)
        veri = response.json()
        
        print(f"\n📊 API Yanıtı:")
        print(f"   HTTP Durum Kodu: {response.status_code}")
        
        if "cod" in veri:
            kod = veri["cod"]
            if kod == 200:
                print(f"\n✅ BAŞARILI! API anahtarınız çalışıyor!")
                print(f"   Şehir: {veri.get('name', 'N/A')}")
                print(f"   Sıcaklık: {veri.get('main', {}).get('temp', 'N/A')}°C")
                return True
            elif kod == 401:
                print(f"\n❌ HATA: Geçersiz API anahtarı (Kod: 401)")
                print(f"   Mesaj: {veri.get('message', 'Bilinmeyen hata')}")
                print(f"\n💡 Çözüm Önerileri:")
                print(f"   1. API anahtarınızı OpenWeatherMap'ten yeniden kopyalayın")
                print(f"   2. API anahtarının başında/sonunda boşluk olmadığından emin olun")
                print(f"   3. API anahtarı yeni oluşturulduysa 10 dakika - 2 saat bekleyin")
                print(f"   4. OpenWeatherMap hesabınızda API anahtarının durumunu kontrol edin")
                return False
            else:
                print(f"\n⚠️  Beklenmeyen yanıt (Kod: {kod})")
                print(f"   Mesaj: {veri.get('message', 'Bilinmeyen hata')}")
                return False
        else:
            print(f"\n⚠️  Yanıt formatı beklenmedik")
            print(f"   Yanıt: {veri}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ İstek hatası: {e}")
        return False

if __name__ == "__main__":
    # API anahtarını al
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("❌ API anahtarı bulunamadı!")
        print("\n.env veya new.env dosyasında OPENWEATHER_API_KEY değişkenini kontrol edin.")
        api_key = input("\nVeya API anahtarınızı buraya yapıştırın: ").strip()
    
    if api_key:
        test_api_key(api_key)
    else:
        print("❌ API anahtarı girilmedi. Program sonlandırılıyor.")

