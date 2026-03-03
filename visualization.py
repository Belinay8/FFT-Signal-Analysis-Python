import matplotlib.pylab as plt 
import numpy as np


def plot_results(t, signal, freqs, fft_mag):
    plt.figure(figsize=(12,5))
    
    #Zaman Grafiği
    plt.subplot(1,2,1)
    # 1 satır 2 sütunluk grafik alanı
    # soldaki grafiği seçiyoruz

    plt.plot(t, signal)  # zaman vs sinyal çiz
    plt.grid(True)
    plt.title("Time Domain Signal")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    #Frekans Grafğı
    plt.subplot(1,2,2)
    plt.plot(freqs, fft_mag)
    plt.grid(True)

    plt.title("Frequency Domain (FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    # En güçlü değerin %30'u üstünü gerçek sinyal kabul ediyoruz
    threshold = max(fft_mag) * 0.3

    # eşikten büyük noktaların indexleri
    peak_indices = np.where(fft_mag > threshold)[0]


    # ==========================
    # GRAFİĞE YAZDIR
    # ==========================
    for i in peak_indices:

        freq = freqs[i]
        mag = fft_mag[i]

    # kırmızı nokta koy
    plt.plot(freq, mag, "ro")

    # frekans değerini yaz
    plt.text(
        freq,
        mag,
        f"{freq:.1f} Hz",
        color="red")

    plt.tight_layout()
    
    plt.show()