from signal_generation import generate_signal
from fft_analysis import compute_fft
from visualization import plot_results 

fs = 1000

t , signal= generate_signal()  # sinyali üret

freqs, fft_mag = compute_fft(signal, fs)  #FFT uygula

plot_results(t, signal, freqs, fft_mag)

print("FFT hesaplandı!")

