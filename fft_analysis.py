import numpy as np

def compute_fft(signal, fs):

    N = len(signal)     #sinyal uzunluğu

    # FFT:
    # "Bu sinyalin içinde hangi frekanslar var?"
    # sorusunun cevabını hesaplar.
    fft_values = np.fft.fft(signal)

    # FFT sonucu karmaşık sayı verir:
    # j kısmı faz bilgisidir.
    # abs() → büyüklük alır
    fft_magnitude = np.abs(fft_values)

    fft_magnitude = fft_magnitude / N  #normalizasyon

    freqs = np.fft.fftfreq(N, 1/fs)    
    # FFT sonucu sayı verir
    # fftfreq bize frekans karşılıklarını üretir.

    return freqs, fft_magnitude
                                       

    