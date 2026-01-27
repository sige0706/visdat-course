


def plot_acceleration_time(acc, fs):
    t = np.arange(len(acc)) / fs

    plt.figure(figsize=(10, 5))
    plt.plot(t, acc)
    plt.xlabel("Zeit [s]")
    plt.ylabel("Beschleunigung")
    plt.title("Beschleunigung über Zeit")
    plt.grid(True)
    plt.show()


def plot_force_time(force, fs):
    t = np.arange(len(force)) / fs

    plt.figure(figsize=(10, 5))
    plt.plot(t, force)
    plt.xlabel("Zeit [s]")
    plt.ylabel("Kraft")
    plt.title("Kraft über Zeit")
    plt.grid(True)
    plt.show()



    

#Plottet den Betrag der Übertragungsfunktion |H(f)|
#def plot_transfer_function(freq, H, f_max, title):
    
#    f_range = (freq >= 0) & (freq <= f_max)

#    plt.figure(figsize=(10, 5))
#    plt.plot(freq[f_range], np.abs(H[f_range]))
#    plt.xlabel("Frequenz")
#    plt.ylabel("Amplitude")
#    plt.title(title)
#    plt.grid(True)
#    #plt.tight_layout()
#    plt.show()




#Vergleich Imaginärteil FFT vs. LabVIEW

#def plot_imaginary_comparison(freq, H, freq_imag, f_max):

#    f_range = (freq >= 0) & (freq <= f_max)

#    H_imag = np.imag(H)             #Imaginärteil Ü-Funktion

#    plt.figure(figsize=(10, 5))
#    plt.plot(freq[f_range], freq_imag[f_range], label="Imaginärteil (CSV / LabVIEW)")
#    plt.plot(freq[f_range], H_imag[f_range], "--", label="Imaginärteil (FFT)")
#    plt.xlabel("Frequenz")
#    plt.ylabel("Im")
#    plt.title("Vergleich der berechneten Imagiärteile und der im LabVIEW abgespeicherten Imaginärteile")
#    plt.legend()
#    plt.grid(True)
#    #plt.tight_layout()
#    plt.show()



#import numpy as np
#import matplotlib.pyplot as plt


#def create_transfer_function_plot(freq, H, f_max, a_max):
#    fig, ax = plt.subplots(figsize=(10, 5))

#    line, = ax.plot(freq, np.abs(H))

#    ax.set_xlim(0, f_max)
#    ax.set_ylim(0, a_max)
#    ax.set_xlabel("Frequenz [Hz]")
#    ax.set_ylabel("Amplitude")
#    ax.set_title("Übertragungsfunktion |H(f)|")
#    ax.grid(True)

#    plt.show(block=False)

#    return fig, ax


#def update_limits(ax, fig, f_max, a_max):
#    ax.set_xlim(0, f_max)
#    ax.set_ylim(0, a_max)
#    fig.canvas.draw_idle()





#import numpy as np
#import matplotlib.pyplot as plt


#def create_transfer_function_plot(freq, H, f_max):
#    fig, ax = plt.subplots(figsize=(10, 5))

#    ax.plot(freq, np.abs(H))

#    ax.set_xlim(0, f_max)
#    ax.set_xlabel("Frequenz [Hz]")
#    ax.set_ylabel("Amplitude")
#    ax.set_title("Übertragungsfunktion |H(f)|")
#    ax.grid(True)

#    plt.show(block=False)

#    return fig, ax


#def update_limits(ax, fig, f_max):
#    ax.set_xlim(0, f_max)
#    fig.canvas.draw_idle()


