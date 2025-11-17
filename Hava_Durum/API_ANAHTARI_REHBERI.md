# 🔑 OpenWeatherMap API Anahtarı Alma ve Kullanma Rehberi

## 📝 Adım 1: OpenWeatherMap Hesabı Oluşturma

1. **Web sitesine gidin:**
   - https://openweathermap.org/ adresine gidin

2. **Ücretsiz hesap oluşturun:**
   - Sağ üst köşedeki **"Sign Up"** veya **"Sign In"** butonuna tıklayın
   - Yeni kullanıcıysanız **"Create an Account"** seçeneğini seçin
   - E-posta adresiniz, kullanıcı adı ve şifre ile kayıt olun
   - E-postanızı doğrulayın (gelen kutunuzu kontrol edin)

## 🔑 Adım 2: API Anahtarı Alma

1. **Giriş yaptıktan sonra:**
   - Sağ üst köşedeki kullanıcı adınıza tıklayın
   - Açılan menüden **"My API keys"** seçeneğine tıklayın
   - Veya doğrudan şu adrese gidin: https://home.openweathermap.org/api_keys

2. **API anahtarı oluşturun:**
   - **"Create key"** butonuna tıklayın
   - Key name (anahtar adı) girin (örn: "Hava Durumu Uygulaması")
   - **"Generate"** butonuna tıklayın
   - ⚠️ **ÖNEMLİ:** API anahtarınızı hemen kopyalayın! (bir daha gösterilmeyebilir)

3. **API anahtarınızı kaydedin:**
   - API anahtarınız uzun bir karakter dizisidir (örn: `520d1eb3eb389cb2014545f47f3f302fc`)
   - Güvenli bir yere kaydedin

## ⏰ API Anahtarı Aktivasyonu

- ⚠️ **ÖNEMLİ:** Yeni oluşturulan API anahtarları genellikle **10 dakika - 2 saat** arasında aktif hale gelir
- İlk kullanımda hata alırsanız, bir süre bekleyip tekrar deneyin

## 💻 Adım 3: API Anahtarını Kullanma

### Yöntem 1: Ortam Değişkeni (Önerilen - Windows PowerShell)

```powershell
# Geçici olarak (sadece bu oturum için)
$env:OPENWEATHER_API_KEY="buraya_api_anahtarinizi_yazin"

# Kalıcı olarak (tüm oturumlar için)
[System.Environment]::SetEnvironmentVariable('OPENWEATHER_API_KEY', 'buraya_api_anahtarinizi_yazin', 'User')
```

**Kullanım:**
1. PowerShell'i açın
2. Yukarıdaki komutu çalıştırın (API anahtarınızı yazın)
3. `python Hava_durumu.py` komutu ile programı çalıştırın

### Yöntem 2: Ortam Değişkeni (Windows CMD)

```cmd
set OPENWEATHER_API_KEY=buraya_api_anahtarinizi_yazin
```

**Kullanım:**
1. CMD'yi açın
2. Yukarıdaki komutu çalıştırın
3. `python Hava_durumu.py` komutu ile programı çalıştırın

### Yöntem 3: .env Dosyası (En Kolay - Önerilen)

1. Proje klasörünüzde `.env` adında bir dosya oluşturun
2. İçine şunu yazın:
   ```
   OPENWEATHER_API_KEY=buraya_api_anahtarinizi_yazin
   ```
3. Program otomatik olarak bu dosyayı okuyacaktır

### Yöntem 4: Program İçinde Giriş

Program çalıştırıldığında API anahtarı bulunamazsa, size soracaktır. O zaman anahtarınızı girebilirsiniz.

## ✅ Test Etme

Programı çalıştırdığınızda:

```bash
python Hava_durumu.py
```

Eğer API anahtarı doğru ayarlanmışsa, şehir sorgulama ekranı gelecektir.

## ❌ Hata Durumları

### "Invalid API key" hatası:
- API anahtarınızı kontrol edin
- API anahtarının aktif olması için 10 dakika - 2 saat bekleyin
- OpenWeatherMap hesabınızda API anahtarının durumunu kontrol edin

### "API key not found" hatası:
- Ortam değişkenini doğru ayarladığınızdan emin olun
- PowerShell/CMD'yi yeniden başlatın (kalıcı ayar için)
- `.env` dosyasının proje klasöründe olduğundan emin olun

## 📊 Ücretsiz Plan Limitleri

OpenWeatherMap'in ücretsiz planı:
- ✅ Dakikada 60 istek
- ✅ Ayda 1 milyon istek
- ✅ Güncel hava durumu
- ✅ 5 günlük tahmin (3 saatlik aralıklarla)

Bu limitler kişisel projeler için yeterlidir.

## 🔒 Güvenlik Uyarısı

⚠️ **ÖNEMLİ:** API anahtarınızı asla:
- GitHub'a yüklemeyin
- Paylaşmayın
- Kod içinde hardcode etmeyin (sadece test için)

`.env` dosyasını `.gitignore` dosyasına ekleyin!

