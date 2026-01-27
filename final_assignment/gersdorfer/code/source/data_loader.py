import pandas as pd
import numpy as np

def load_measurement_csv(file_path, header_rows, acc_col, force_col, freq_imag_col):
    data = pd.read_csv(
    file_path,
    sep="\t",
    decimal=",",
    skiprows=header_rows
    )

    freq_imag = data[freq_imag_col]
    acc_timedata = data[acc_col]
    force_timedata = data[force_col]


    return freq_imag, acc_timedata, force_timedata





#import pandas as pd


#def load_measurement_csv(
#    file_path,
#    header_rows,
#    acc_col,
#    force_col,
#    imag_col=None
#):
#    data = pd.read_csv(
#        file_path,
#        sep="\t",
#        decimal=",",
#        skiprows=header_rows
#    )

#    acc = data[acc_col].to_numpy()
#    force = data[force_col].to_numpy()

#    freq_imag = None
#    if imag_col is not None:
#        freq_imag = data[imag_col].to_numpy()
#
#    return freq_imag, acc, force
