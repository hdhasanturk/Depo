"""
Hava Durumu Uygulaması
OpenWeatherMap API kullanarak şehir bazlı hava durumu bilgisi gösterir.
"""

import requests
import json
import os
from datetime import datetime

# .env dosyası desteği için
try:
    from dotenv import load_dotenv
    # .env dosyasını yükle (new.env, .env gibi farklı isimleri de dene)
    load_dotenv('.env')  # Önce .env dosyasını dene
    load_dotenv('new.env', override=False)  # Sonra new.env dosyasını dene (override=False: önceki değerleri korur)
except ImportError:
    # python-dotenv yüklü değilse, manuel olarak new.env dosyasını oku
    try:
        if os.path.exists('new.env'):
            with open('new.env', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('OPENWEATHER_API_KEY='):
                        api_key_value = line.split('=', 1)[1].strip()
                        os.environ['OPENWEATHER_API_KEY'] = api_key_value
                        break
        elif os.path.exists('.env'):
            with open('.env', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('OPENWEATHER_API_KEY='):
                        api_key_value = line.split('=', 1)[1].strip()
                        os.environ['OPENWEATHER_API_KEY'] = api_key_value
                        break
    except Exception:
        pass


class HavaDurumu:
    """Hava durumu bilgilerini OpenWeatherMap API'den çeken sınıf"""
    
    def __init__(self, api_key):
        """
        Args:
            api_key (str): OpenWeatherMap API anahtarı
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def hava_durumu_getir(self, sehir, dil="tr", birim="metric"):
        """
        Belirtilen şehir için hava durumu bilgilerini getirir.
        
        Args:
            sehir (str): Şehir adı
            dil (str): Dil kodu (varsayılan: tr)
            birim (str): Sıcaklık birimi (metric: Celsius, imperial: Fahrenheit)
        
        Returns:
            dict: Hava durumu bilgileri veya None (hata durumunda)
        """
        params = {
            "q": sehir,
            "appid": self.api_key,
            "lang": dil,
            "units": birim
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            veri = response.json()
            
            # API hata mesajlarını kontrol et
            if "cod" in veri and veri["cod"] != 200:
                hata_kodu = veri.get("cod", "Bilinmeyen")
                hata_mesaji = veri.get("message", "Bilinmeyen hata")
                
                if hata_kodu == 401:
                    print(f"❌ API Anahtarı Hatası: Geçersiz API anahtarı!")
                    print("💡 API anahtarınızı kontrol edin veya yeni bir anahtar oluşturun.")
                elif hata_kodu == 404:
                    print(f"❌ Şehir Bulunamadı: '{sehir}' için hava durumu bilgisi bulunamadı.")
                    print("💡 Şehir adını kontrol edin veya 'Şehir, Ülke' formatında deneyin (örn: Istanbul, TR)")
                else:
                    print(f"❌ API Hatası (Kod: {hata_kodu}): {hata_mesaji}")
                
                return None
            
            # Başarılı yanıt
            return veri
            
        except requests.exceptions.Timeout:
            print("❌ İstek zaman aşımına uğradı. İnternet bağlantınızı kontrol edin.")
            return None
        except requests.exceptions.ConnectionError:
            print("❌ İnternet bağlantısı hatası. İnternet bağlantınızı kontrol edin.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ API isteği başarısız: {e}")
            return None
        except json.JSONDecodeError:
            print("❌ API yanıtı okunamadı. Geçersiz veri formatı.")
            return None
    
    def bilgileri_goster(self, veri):
        """
        Hava durumu bilgilerini kullanıcı dostu formatta gösterir.
        
        Args:
            veri (dict): API'den dönen hava durumu verisi
        """
        if not veri:
            print("❌ Hava durumu bilgisi alınamadı.")
            return
        
        try:
            # Temel bilgiler
            sehir = veri["name"]
            ulke = veri["sys"]["country"]
            sicaklik = veri["main"]["temp"]
            hissedilen = veri["main"]["feels_like"]
            nem = veri["main"]["humidity"]
            basinc = veri["main"]["pressure"]
            ruzgar_hizi = veri["wind"]["speed"]
            aciklama = veri["weather"][0]["description"].title()
            icon = veri["weather"][0]["icon"]
            
            # Gün doğumu ve batımı
            gun_dogumu = datetime.fromtimestamp(veri["sys"]["sunrise"]).strftime("%H:%M")
            gun_batimi = datetime.fromtimestamp(veri["sys"]["sunset"]).strftime("%H:%M")
            
            # Çıktıyı formatla
            print("\n" + "="*50)
            print(f"🌤️  HAVA DURUMU - {sehir.upper()}, {ulke}")
            print("="*50)
            print(f"📊 Durum: {aciklama}")
            print(f"🌡️  Sıcaklık: {sicaklik:.1f}°C")
            print(f"🤲 Hissedilen: {hissedilen:.1f}°C")
            print(f"💧 Nem: %{nem}")
            print(f"📉 Basınç: {basinc} hPa")
            print(f"💨 Rüzgar Hızı: {ruzgar_hizi} m/s")
            print(f"🌅 Gün Doğumu: {gun_dogumu}")
            print(f"🌇 Gün Batımı: {gun_batimi}")
            print("="*50 + "\n")
            
        except KeyError as e:
            print(f"❌ Veri formatı hatası: {e} eksik alan bulundu.")


def main():
    """Ana program fonksiyonu"""
    print("="*50)
    print("🌤️  HAVA DURUMU UYGULAMASI")
    print("="*50)
    
    # API anahtarını al ve temizle
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("\n⚠️  API anahtarı bulunamadı!")
        print("Lütfen aşağıdaki adımları takip edin:")
        print("1. https://openweathermap.org/api adresinden ücretsiz API anahtarı alın")
        print("2. API anahtarınızı .env dosyasına ekleyin (new.env dosyası da desteklenir)")
        print("3. Ortam değişkeni olarak ayarlayın: set OPENWEATHER_API_KEY=your_key")
        print("\nAlternatif olarak, API anahtarınızı buraya girebilirsiniz:")
        api_key = input("API Anahtarı: ").strip()
        
        if not api_key:
            print("❌ API anahtarı gerekli. Program sonlandırılıyor.")
            return
    
    # API anahtarını temizle (başındaki/sonundaki boşlukları ve görünmez karakterleri kaldır)
    api_key = api_key.strip()
    
    # API anahtarı uzunluğunu kontrol et
    if len(api_key) < 20:
        print(f"⚠️  UYARI: API anahtarı çok kısa görünüyor ({len(api_key)} karakter)")
        print("💡 API anahtarları genellikle 32 karakter uzunluğundadır.")
        print("💡 API anahtarınızı kontrol edin ve tekrar deneyin.")
    
    # API anahtarını test et
    print(f"✅ API anahtarı yüklendi: {api_key[:8]}...{api_key[-4:]} (Toplam: {len(api_key)} karakter)")
    print("🔍 API anahtarı test ediliyor...")
    
    try:
        # Test isteği gönder
        test_hava_durumu = HavaDurumu(api_key)
        test_veri = test_hava_durumu.hava_durumu_getir("London", dil="en")
        
        if test_veri and isinstance(test_veri, dict):
            if "cod" in test_veri:
                kod = test_veri["cod"]
                if kod == 200:
                    print("✅ API anahtarı çalışıyor! Uygulama kullanıma hazır.\n")
                elif kod == 401:
                    print("\n❌ API ANAHTARI HATASI TESPİT EDİLDİ!")
                    print("="*50)
                    print("🔍 Olası Nedenler:")
                    print("1. API anahtarı henüz aktif olmamış olabilir (10 dakika - 2 saat bekleyin)")
                    print("2. API anahtarında boşluk veya görünmez karakterler olabilir")
                    print("3. API anahtarı yanlış kopyalanmış olabilir")
                    print("4. OpenWeatherMap hesabınızda API anahtarının durumunu kontrol edin")
                    print("\n💡 Çözüm Önerileri:")
                    print("- OpenWeatherMap sitesine giriş yapın: https://home.openweathermap.org/api_keys")
                    print("- API anahtarınızı yeniden kopyalayın (tam olarak)")
                    print("- .env dosyasını kontrol edin (boşluk olmamalı)")
                    print("- Birkaç saat bekleyip tekrar deneyin")
                    print("="*50)
                    print("\n⚠️  Devam etmek istiyor musunuz? (e/h): ", end="")
                    devam = input().strip().lower()
                    if devam != 'e':
                        print("👋 Program sonlandırılıyor.")
                        return
                else:
                    mesaj = test_veri.get("message", "Bilinmeyen hata")
                    print(f"⚠️  API test hatası (Kod: {kod}): {mesaj}")
                    print("⚠️  Devam ediliyor...\n")
            else:
                # cod yoksa başarılı olabilir
                print("✅ API anahtarı test edildi. Devam ediliyor...\n")
        else:
            print("⚠️  API anahtarı test edilemedi. Devam ediliyor...\n")
    except Exception as e:
        print(f"⚠️  Test sırasında hata oluştu: {e}")
        print("⚠️  Devam ediliyor...\n")
    
    hava_durumu = HavaDurumu(api_key)
    
    # Ana döngü
    while True:
        print("\n" + "-"*50)
        sehir = input("🌍 Şehir adını girin (çıkmak için 'q'): ").strip()
        
        if sehir.lower() == 'q':
            print("\n👋 Program sonlandırılıyor. İyi günler!")
            break
        
        if not sehir:
            print("⚠️  Lütfen geçerli bir şehir adı girin.")
            continue
        
        print(f"\n⏳ {sehir} için hava durumu bilgileri alınıyor...")
        veri = hava_durumu.hava_durumu_getir(sehir)
        
        if veri:
            # API yanıtında hata kontrolü
            if "cod" in veri and veri["cod"] == 200:
                hava_durumu.bilgileri_goster(veri)
            elif "cod" in veri:
                # Hata mesajı zaten hava_durumu_getir içinde gösterildi
                pass
            else:
                # Yanıt formatı beklenmedik, yine de göster
                hava_durumu.bilgileri_goster(veri)


if __name__ == "__main__":
    main()


