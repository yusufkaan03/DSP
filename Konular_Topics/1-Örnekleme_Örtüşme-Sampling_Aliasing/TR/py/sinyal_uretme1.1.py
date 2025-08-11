#!/usr/bin/env python3
# Amaç: Tek bir sinüs sinyali üret, zaman grafiğini kaydet, basit doğrulama yap.

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

f0 = 100.0    #Sinüs frekansı [Hz]
A = 1       #Genlik
phi = np.pi/2   #faz[rad]
T_sinyal = 0.04

# Bilgisayar ortamında sürekli bir sinyal imkansız olduğu için sürekli gibi bir sinyal oluşturacağız

dt = 1e-5

t = np.arange(0, T_sinyal, dt)

x = A * np.sin(2.0 * np.pi * f0 * t + phi)

figs_dir = Path(__file__).resolve().parents[1] / "figs"
figs_dir.mkdir(parents=True, exist_ok=True)
out_png = figs_dir / "SurekliGibi.png"

plt.figure(figsize=(9,3))
plt.plot(t,x)
plt.title(f"Yaklaşık sürekli sinüs dalgası f0: {f0}Hz, dt: {dt}s")
plt.xlabel("Zaman(s)")
plt.ylabel("Genlik")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out_png, dpi=150)
plt.close()

#N = f0*2 #Nyquist Frekansı

ornek = T_sinyal*f0

ornek_sayisi_f0 = int(ornek)
ornek_sayisi_2f0 = 2*ornek_sayisi_f0
ornek_sayisi_4f0 = 4*ornek_sayisi_f0
ornek_sayisi_8f0 = 8*ornek_sayisi_f0

uzx = int(len(x))

xp1f0 = np.zeros(uzx)
xp2f0 = np.zeros(uzx)
xp4f0 = np.zeros(uzx)
xp8f0 = np.zeros(uzx)

adimf0 = int(len(x)/ornek_sayisi_f0)
adim2f0 = int(len(x)/ornek_sayisi_2f0)
adim4f0 = int(len(x)/ornek_sayisi_4f0)
adim8f0 = int(len(x)/ornek_sayisi_8f0)


for i in range (0, uzx-1, adimf0):
    xp1f0[i] = x[i]
    print(i)

for i in range (0, uzx-1, adim2f0):
    xp2f0[i] = x[i]

for i in range (0, uzx-1, adim4f0):
    xp4f0[i] = x[i]

for i in range (0, uzx-1, adim8f0):
    xp8f0[i] = x[i]

xp_list = [xp1f0, xp2f0, xp4f0, xp8f0]
os_list = [ornek_sayisi_f0, ornek_sayisi_2f0, ornek_sayisi_4f0, ornek_sayisi_8f0]

for i in range (0,4):
    figs_dir = Path(__file__).resolve().parents[1] / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)
    out_png = figs_dir / f"Orneklenmis{2**i}f0(len ile).png"

    plt.figure(figsize=(9, 3))
    plt.plot(t, xp_list[i])
    plt.title(f"Frekasın {2**i} katı ile (fo: {f0*(2**i)}Hz). Ornek sayısı: {os_list[i]}" )
    plt.xlabel("Zaman(s)")
    plt.ylabel("Genlik")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)
    plt.close()


