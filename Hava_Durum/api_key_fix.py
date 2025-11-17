"""
API Anahtarı Düzeltme ve Doğrulama Scripti
API anahtarınızı kontrol eder ve düzeltmenize yardımcı olur.
"""

import requests
import os
import re

def temizle_api_key(api_key):
    """API anahtarını temizler"""
    # Başındaki/sonundaki boşlukları kaldır
    api_key = api_key.strip()
    # Tırnak işaretlerini kaldır
    api_key = api_key.strip('"').strip("'")
    return api_key

def dogrula_api_key_format(api_key):
    """API anahtarının formatını doğrular"""
    # API anahtarı genellikle 32 karakter uzunluğunda alfanumerik bir string'dir
    if len(api_key) < 20:
        return False, f"API anahtarı çok kısa ({len(api_key)} karakter). Genellikle 32 karakter olmalıdır."
    
    if len(api_key) > 50:
        return False, f"API anahtarı çok uzun ({len(api_key)} karakter). Genellikle 32 karakter olmalıdır."
    
    # Sadece harf, rakam ve bazı özel karakterler içermeli
    if not re.match(r'^[a-zA-Z0-9]+$', api_key):
        return False, "API anahtarı sadece harf ve rakam içermelidir."
    
    return True, "Format doğru görünüyor."

def test_api_key(api_key):
    """API anahtarını test eder"""
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "London",
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        veri = response.json()
        
        if "cod" in veri:
            kod = veri["cod"]
            if kod == 200:
                return True, "API anahtarı çalışıyor!", veri
            elif kod == 401:
                return False, "Geçersiz API anahtarı (401)", veri.get("message", "")
            else:
                return False, f"API hatası (Kod: {kod})", veri.get("message", "")
        else:
            return False, "Beklenmeyen yanıt formatı", str(veri)
            
    except requests.exceptions.RequestException as e:
        return False, f"İstek hatası: {e}", ""

def main():
    print("="*70)
    print("🔧 API ANAHTARI DÜZELTME VE DOĞRULAMA ARACI")
    print("="*70)
    
    # .env dosyasını yükle
    try:
        from dotenv import load_dotenv
        if not load_dotenv('.env'):
            load_dotenv('new.env')
    except ImportError:
        print("⚠️  python-dotenv yüklü değil. Ortam değişkenlerinden okunuyor...")
    
    # API anahtarını al
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("\n❌ API anahtarı bulunamadı!")
        print("\n.env veya new.env dosyasında OPENWEATHER_API_KEY değişkenini kontrol edin.")
        api_key = input("\nVeya API anahtarınızı buraya yapıştırın: ")
    
    if not api_key:
        print("❌ API anahtarı girilmedi. Program sonlandırılıyor.")
        return
    
    print("\n" + "="*70)
    print("📋 ADIM 1: API ANAHTARI TEMİZLENİYOR")
    print("="*70)
    
    # API anahtarını temizle
    orijinal_uzunluk = len(api_key)
    api_key_temiz = temizle_api_key(api_key)
    temizlenmis_uzunluk = len(api_key_temiz)
    
    print(f"Orijinal uzunluk: {orijinal_uzunluk} karakter")
    print(f"Temizlenmiş uzunluk: {temizlenmis_uzunluk} karakter")
    
    if orijinal_uzunluk != temizlenmis_uzunluk:
        print("⚠️  API anahtarında gereksiz karakterler bulundu ve temizlendi!")
        print(f"Temizlenmiş API anahtarı: {api_key_temiz[:8]}...{api_key_temiz[-4:]}")
    else:
        print(f"✅ API anahtarı temiz görünüyor: {api_key_temiz[:8]}...{api_key_temiz[-4:]}")
    
    print("\n" + "="*70)
    print("📋 ADIM 2: API ANAHTARI FORMATI KONTROL EDİLİYOR")
    print("="*70)
    
    # Format kontrolü
    format_ok, format_mesaj = dogrula_api_key_format(api_key_temiz)
    if format_ok:
        print(f"✅ {format_mesaj}")
    else:
        print(f"❌ {format_mesaj}")
        print("\n💡 API anahtarınızı OpenWeatherMap'ten yeniden kopyalayın.")
        return
    
    print("\n" + "="*70)
    print("📋 ADIM 3: API ANAHTARI TEST EDİLİYOR")
    print("="*70)
    
    # API anahtarını test et
    basarili, mesaj, detay = test_api_key(api_key_temiz)
    
    if basarili:
        print(f"\n✅ {mesaj}")
        print(f"   Test şehri: {detay.get('name', 'N/A')}")
        print(f"   Sıcaklık: {detay.get('main', {}).get('temp', 'N/A')}°C")
        print("\n" + "="*70)
        print("✅ BAŞARILI! API anahtarınız çalışıyor!")
        print("="*70)
        print("\n💡 .env dosyanıza temizlenmiş API anahtarını yazın:")
        print(f"OPENWEATHER_API_KEY={api_key_temiz}")
    else:
        print(f"\n❌ {mesaj}")
        if detay:
            print(f"   Detay: {detay}")
        
        print("\n" + "="*70)
        print("❌ API ANAHTARI ÇALIŞMIYOR")
        print("="*70)
        print("\n🔍 Olası Nedenler:")
        print("1. API anahtarı henüz aktif olmamış (10 dakika - 2 saat bekleyin)")
        print("2. API anahtarı geçersiz veya yanlış kopyalanmış")
        print("3. OpenWeatherMap hesabınızda sorun var")
        print("\n💡 Çözüm Önerileri:")
        print("1. https://home.openweathermap.org/api_keys adresine gidin")
        print("2. Yeni bir API anahtarı oluşturun")
        print("3. API anahtarını tam olarak kopyalayın")
        print("4. .env dosyasına şu formatta yazın:")
        print("   OPENWEATHER_API_KEY=api_anahtariniz_buraya")
        print("   (Eşittir işaretinden sonra boşluk OLMAMALI)")
        print("5. Birkaç saat bekleyip tekrar deneyin")

if __name__ == "__main__":
    main()

