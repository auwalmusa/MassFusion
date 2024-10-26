# src/visualization/plot_manager.py
import matplotlib.pyplot as plt

class PlotManager:
    def __init__(self, data):
        """
        Initializes the PlotManager with signal data.
        
        Parameters:
        - data (array): Signal data to plot.
        """
        self.data = data

    def plot_chromatogram(self):
        """
        Plots a chromatogram showing intensity over time or index.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.data, label='Chromatogram')
        plt.xlabel("Index")
        plt.ylabel("Intensity")
        plt.title("Chromatogram")
        plt.legend()
        plt.show()

    def plot_mass_spectrum(self, features):
        """
        Plots a mass spectrum based on detected features.
        
        Parameters:
        - features (list): List of detected features with m/z and intensity.
        """
        plt.figure(figsize=(10, 5))
        mz_values = [feature["m/z"] for feature in features]
        intensities = [feature["intensity"] for feature in features]
        plt.stem(mz_values, intensities, basefmt=" ", label='Mass Spectrum')  # Removed use_line_collection
        plt.xlabel("m/z")
        plt.ylabel("Intensity")
        plt.title("Mass Spectrum")
        plt.legend()
        plt.show()
