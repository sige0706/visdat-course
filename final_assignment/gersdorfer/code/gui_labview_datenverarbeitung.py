from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QFileDialog, QLineEdit, QMessageBox
)

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT
)

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'source')))

from matplotlib.figure import Figure
import numpy as np



import data_loader as dl
import signal_processing as sp
from export_dialog import ExportCSVDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FFT Analyse Tool")
        self.resize(1000, 700)

        self.file_path = None
        self.available_signals = None

        # ---------- Zentrales Widget ----------
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # ---------- Datei ----------
        self.label = QLabel("Keine Datei ausgewählt")
        layout.addWidget(self.label)

        btn_open = QPushButton("CSV-Datei auswählen")
        btn_open.clicked.connect(self.open_file)
        layout.addWidget(btn_open)

        # ---------- Parameter ----------
        layout.addWidget(QLabel("Samplingfrequenz [Hz]:"))
        self.fs_input = QLineEdit("12800")
        layout.addWidget(self.fs_input)

        layout.addWidget(QLabel("Header-Zeilen überspringen:"))
        self.header_input = QLineEdit("22")
        layout.addWidget(self.header_input)

        layout.addWidget(QLabel("Spalte Acceleration:"))
        self.acc_input = QLineEdit("Acceleration")
        layout.addWidget(self.acc_input)

        layout.addWidget(QLabel("Spalte Force:"))
        self.force_input = QLineEdit("Force")
        layout.addWidget(self.force_input)

        layout.addWidget(QLabel("Spalte Imaginärteil:"))
        self.imag_input = QLineEdit("Untitled")
        layout.addWidget(self.imag_input)

        # ---------- Buttons ----------
        btn_plot = QPushButton("Übertragungsfunktion plotten")
        btn_plot.clicked.connect(self.run_analysis)
        layout.addWidget(btn_plot)

        self.btn_export = QPushButton("CSV exportieren")
        self.btn_export.setEnabled(False)
        self.btn_export.clicked.connect(self.export_csv)
        layout.addWidget(self.btn_export)

        # ---------- Plot ----------
        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvasQTAgg(self.figure)
        layout.addWidget(self.canvas)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        layout.addWidget(self.toolbar)

        self.ax = self.figure.add_subplot(111)

    # ---------- Datei auswählen ----------
    def open_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self,
            "CSV auswählen",
            "",
            "CSV Files (*.csv)"
        )
        if self.file_path:
            self.label.setText(self.file_path)

    # ---------- Analyse ----------
    def run_analysis(self):
        if not self.file_path:
            QMessageBox.warning(self, "Fehler", "Bitte zuerst eine Datei auswählen.")
            return

        try:
            fs = float(self.fs_input.text())
            header_rows = int(self.header_input.text())
        except ValueError:
            QMessageBox.warning(self, "Eingabefehler", "Samplingfrequenz oder Header-Zeilen ungültig.")
            return

        acc_col = self.acc_input.text()
        force_col = self.force_input.text()
        imag_col = self.imag_input.text()

        try:
            freq_imag, acc, force = dl.load_measurement_csv(
                self.file_path,
                header_rows,
                acc_col,
                force_col,
                imag_col
            )
        except Exception as e:
            QMessageBox.critical(self, "Ladefehler", str(e))
            return

        freq, H = sp.compute_fft(acc, force, fs)

        # Zeitachse
        time = np.arange(len(acc)) / fs

        # ---------- verfügbare Signale ----------
        self.available_signals = {
            "time": time,
            "frequency": freq,
            "acceleration": acc,
            "force": force,
            "H_abs": np.abs(H),
            "H_phase": np.angle(H),
            "H_real": np.real(H),
            "H_imag": np.imag(H),
        }

        # ---------- Plot ----------
        self.ax.clear()
        self.ax.plot(freq, np.abs(H))
        self.ax.set_xlim(0, 40)
        self.ax.set_xlabel("Frequenz [Hz]")
        self.ax.set_ylabel("Amplitude")
        self.ax.set_title("Übertragungsfunktion |H(f)|")
        self.ax.grid(True)
        self.canvas.draw()

        self.btn_export.setEnabled(True)

    # ---------- CSV Export ----------
    def export_csv(self):
        if not self.available_signals:
            return

        dialog = ExportCSVDialog(self.available_signals, self)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
