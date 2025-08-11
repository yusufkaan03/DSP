# 1 – Örnekleme & Örtüşme (Sampling & Aliasing)

## Amaç
Sürekli zamanlı bir sinyalin belirli aralıklarla (T) örneklenmesi sonucu frekans alanında periyodiklik oluştuğunu ve Nyquist sınırının aşılması durumunda aliasing (örtüşme) etkisini gözlemlemek.

## Görevler
- [ ] 3 sinüs + gürültü sinyali üretmek (50 Hz, 220 Hz, 500 Hz)
- [ ] Hann penceresi ile FFT alarak spektrumu çizmek
- [ ] Aliasing’in zaman alanındaki görünümünü oluşturmak
- [ ] Python kodunu `py/fft_ornekleme_ortusme.py` dosyasında çalıştırmak
- [ ] Görselleri `figs/` klasörüne kaydetmek:
  - `fft_spektrumu.png`
  - `aliasing_zaman_alani.png`
- [ ] (STM32 – Yarın) ADC ile ≥512 örnek toplamak, `data/raw/adc_ornekleme.csv` olarak kaydetmek
- [ ] README ve teori dosyalarını güncellemek

## Doğrulama Ölçütleri
- FFT’de 50 Hz ve 220 Hz pikleri ±%10 tolerans içinde
- 500 Hz bileşeni yerine 300 Hz alias piki görülmeli
- ADC verisinde örnek sayısı ≥512
- README ve teori dosyası güncel

## Beklenen Çıktılar
- `figs/fft_spektrumu.png`  
- `figs/aliasing_zaman_alani.png`  
- `data/raw/adc_ornekleme.csv` (STM32 çalışmasından sonra)

## Teori
Ayrıntılı formüller, açıklamalar ve diyagramlar için [teori.md](teori.md) dosyasına bakınız.

## Notlar
- Python kodları `py/` klasöründe tutulur.
- STM32 kodları `embedded/` klasöründe tutulur.
- Ham veriler `data/raw/` klasöründe, işlenmiş veriler `data/processed/` klasöründe bulunur.
