import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'source')))



#from data_loader import load_measurement_csv                #Aufrufen der Daten-Einlese Funktion
#from signal_processing import compute_fft                   #Aufrufen der FFT Funktion
#from plotter import plot_transfer_function
#from plotter import plot_imaginary_comparison

import data_loader as dl
import signal_processing as sp
import plotter  as plo



file_path = "C:/Users/Simon/github/visdat-course/final_assignment/gersdorfer/code/data/P2b_OhneTilger.csv"
header_rows = 22
acc_col = ("Acceleration")
force_col = ("Force")
freq_imag_col = ("Untitled")

# Ausführung der Einlese Funktion
freq_imag, acc_timedata, force_timedata  = dl.load_measurement_csv(file_path, header_rows, acc_col, force_col, freq_imag_col)


fs = 12800              #Gewählte Abtastrate der Messung

# Ausführung der FFT Funktion
freq, H = sp.compute_fft(acc_timedata, force_timedata, fs)




#Parameter Visualisierung
f_max = 40                              #Maximale Frequenz der Visualisierung
f_range= (freq>=0) & (freq <=f_max)     #Dargestellter Frequenzbereich



# Plots
plo.plot_transfer_function(freq, H, f_max, title="Übertragungsfunktion Betrag – Ohne Tilger")

plo.plot_imaginary_comparison(freq, H, freq_imag, f_max)