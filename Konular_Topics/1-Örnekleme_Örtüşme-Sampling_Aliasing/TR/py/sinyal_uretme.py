#!/usr/bin/env python3
# Amaç: Tek bir sinüs sinyali üret, zaman grafiğini kaydet, basit doğrulama yap.

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------ 1) Parametreler ------------------
fs = 2000.0   # örnekleme frekansı [Hz] -> saniyede kaç örnek
T  = 1.0      # kayıt süresi [s]
f0 = 50.0     # sinüs frekansı [Hz]
A  = 1.0      # genlik (tepe)
phi = 0.0     # faz [rad]

# ------------------ 2) Zaman dizisi ------------------
# N = fs * T kadar örnek olur. dt = 1/fs örnek aralığıdır.
N  = int(fs * T)
dt = 1.0 / fs
t  = np.arange(N) * dt  # [0, dt, 2dt, ...] uzunluk N

# ------------------ 3) Sinyal üretimi ----------------
# x[n] = A * sin(2π f0 t[n] + phi)
x = A * np.sin(2.0 * np.pi * f0 * t + phi)

# ------------------ 4) Zaman grafiği -----------------
# İlk 0.1 saniyeyi çizelim ki dalga formu net görünsün.
view_samples = int(0.1 * fs)  # 0.1 s * fs örnek
figs_dir = Path(__file__).resolve().parents[1] / "figs"
figs_dir.mkdir(parents=True, exist_ok=True)
out_png = figs_dir / "1.sinyal.png"

plt.figure(figsize=(9,3))
plt.plot(t[:view_samples], x[:view_samples])
plt.title(f"Tek Sinüs: f0={f0} Hz, fs={fs} Hz, N={N}")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out_png, dpi=150)
plt.close()

# ------------------ 5) Basit doğrulamalar ------------
# (a) Uzunluk kontrolü
ok_len = (len(x) == N)

# (b) Genlik ~ A (pencere yokken tepe yaklaşık A olur)
x_peak = np.max(np.abs(x))
ok_amp = (abs(x_peak - A) <= 0.10 * A)  # ±%10 tolerans

# (c) Örnekleme/frekans çözünürlüğü bilgisi
# Burada sadece bilgilendiriyoruz; FFT'ye yarın geçeceğiz.
df = 1.0 / T  # N = fs*T olduğundan FFT çözünürlüğü ~ 1/T olur

print("[BİLGİ] fs=", fs, "Hz | T=", T, "s | N=", N, "örnek | dt=", dt, "s")
print("[BİLGİ] Beklenen frekans çözünürlüğü (FFT için): Δf≈", df, "Hz")
print("[DOĞRULAMA] Uzunluk N doğru mu? ->", "OK" if ok_len else "HATALI")
print("[DOĞRULAMA] Tepe genlik ≈ A (±%10)? ->", "OK" if ok_amp else f"HATALI (peak={x_peak:.3f})")
print("[ÇIKTI]", out_png)
