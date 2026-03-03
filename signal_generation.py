import numpy as np

def generate_signal():      
    fs = 1000   #sampling f , 1sn de 1000 kez örnek al
    T = 1         #signal duration (seconds)

    t = np.linspace(0, T, fs)

    f1 = 50      #farklı frekansta iki sinyal oluşturuyoruz
    f2 = 120

    signal =  (
        np.sin(2*np.pi*f1*t) +
        0.5*np.sin(2*np.pi*f2*t)
    )
    return t, signal