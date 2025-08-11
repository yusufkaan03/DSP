import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

fs = 100.0
A = 1
phi = np.pi/2
T = 0.04

dt = 1e-5

t = np.arange(0, T, dt)

x = A*np.sin(2.0 * np.pi * fs *t + phi)

figs_dos = Path(__file__).resolve().parents[1]/ "figs"
figs_dos.mkdir(parents=True, exist_ok=True)
cik_png = figs_dos / "OrneklenecekSinyal.png"

plt.figure(figsize=(9,3))
plt.plot(t,x)
plt.title(f"Sinyal f0: {fs}Hz, dt: {dt}s")
plt.xlabel("Zaman(s)")
plt.ylabel("Genlik")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(cik_png, dpi=150)
plt.close()

def sample_with_fs(x, t, fs_samp, dt, T):
    N = int(T*fs_samp)
    t_s = np.arange(N)/fs_samp
    idx = np.clip(np.round(t_s/dt).astype(int), 0, len(x)-1)
    x_s = x[idx]
    return t_s, x_s

for sample in [1, 2, 4, 8, 16]:
    fs_s = fs*sample
    t_s, x_s = sample_with_fs(x, t, fs_s, dt, T)

    cik_png = figs_dos / f"OrneklenmişFrekans_{sample}*fs.png"
    plt.figure(figsize=(9,3))
    plt.plot(t, x, alpha = 1, lw = 1)
    plt.plot(t_s, x_s, linestyle = 'none', marker = 'o', ms = 2)
    plt.title(f"{sample}*fs ile örnekleme (fs={fs_s:.1f}Hz) - örnek sayısı={len(x_s)}")
    plt.xlabel("Zaman(s)")
    plt.ylabel("Genlik")
    plt.vlines(t_s, 0, x_s, colors='orange', linestyles='dashed')
    plt.grid(True, alpha = 0.3)
    plt.tight_layout()
    plt.savefig(cik_png, dpi=200)
    plt.close()

    print(f"fs={fs_s:.1f} Hz → N={len(x_s)} örnek, ilk 5: {np.round(x_s[:5], 3)}")








