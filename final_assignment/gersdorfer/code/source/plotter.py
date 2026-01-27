import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




###Nur für Main File
def plot_transfer_function(freq, H, f_max, title):
    f_range = (freq >= 0) & (freq <= f_max)

    plt.figure(figsize=(10, 5))
    plt.plot(freq[f_range], np.abs(H[f_range]))
    plt.xlabel("Frequenz [Hz]")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_imaginary_comparison(freq, H, freq_imag, f_max):
    f_range = (freq >= 0) & (freq <= f_max)

    H_imag = np.imag(H)

    plt.figure(figsize=(10, 5))
    plt.plot(freq[f_range], freq_imag[f_range], label="CSV / LabVIEW")
    plt.plot(freq[f_range], H_imag[f_range], "--", label="FFT")
    plt.xlabel("Frequenz [Hz]")
    plt.ylabel("Im")
    plt.title("Imaginärteil Vergleich")
    plt.legend()
    plt.grid(True)
    plt.show()