# F10 SS — Monitör & Tuş Seçimli Ekran Görüntüsü Aracı

[![Live Demo](https://img.shields.io/badge/🌐_Canlı_Demo-GitHub_Pages-1f6feb?style=for-the-badge)](https://eren-oztk.github.io/f10_ss)
[![Language](https://img.shields.io/badge/Python-100%25-3776AB?style=for-the-badge&logo=python)](https://github.com/Eren-Oztk/f10_ss)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)](https://github.com/Eren-Oztk/f10_ss)

Birden fazla monitörünüz varsa, istediğiniz monitörden istediğiniz tuşla ekran görüntüsü almanızı sağlayan hafif bir masaüstü uygulaması.

## Özellikler

- Birden fazla monitör algılama ve seçme
- Özelleştirilebilir kısayol tuşu (F9, F10, F11, F12, Print Screen, Insert, Home)
- Otomatik sıralı dosya adlandırma (`ss_001.png`, `ss_002.png`, …)
- Kayıt klasörü seçimi
- Başlat / Durdur kontrolü
- Sıfır bağımlılıklı `.exe` (PyInstaller ile derlendi)

## Kurulum

### Kaynak koddan çalıştırma

```bash
pip install -r requirements.txt
python ss_f10.py
```

### Hazır .exe (Windows)

[Releases](../../releases) sayfasından `ss_f10.exe` dosyasını indirip doğrudan çalıştırın. Kurulum gerekmez.

## Kullanım

1. **Klasör Seç** — ekran görüntülerinin kaydedileceği klasörü seçin
2. **Monitör Seç** — hangi ekranın fotoğraflanacağını seçin
3. **Tuş Seç** — tetikleyici kısayol tuşunu seçin (varsayılan: F10)
4. **Başlat** — arka planda dinlemeye geçer
5. Seçtiğiniz tuşa basın — görüntü otomatik kaydedilir
6. **Durdur** — dinlemeyi sonlandırır

## Gereksinimler

| Paket | Açıklama |
|-------|----------|
| `mss` | Hızlı ekran görüntüsü kütüphanesi |
| `keyboard` | Global tuş dinleme |

`tkinter` Python ile birlikte gelir, ayrıca kurulum gerekmez.

## .exe Derleme

```bash
pip install pyinstaller
pyinstaller ss_f10.spec
```

Çıktı: `dist/ss_f10.exe`

## Lisans

MIT
