# src/visualization/ion_maps.py
import matplotlib.pyplot as plt

class IonMap:
    def __init__(self, features, retention_times):
        """
        Initializes the IonMap with features and retention times.
        
        Parameters:
        - features (list): List of detected features with m/z and intensity.
        - retention_times (array): Array of retention times or indices.
        """
        self.features = features
        self.retention_times = retention_times

    def plot_ion_map(self):
        """
        Plots an ion map of m/z vs. retention time.
        """
        mz_values = [feature["m/z"] for feature in self.features]
        intensities = [feature["intensity"] for feature in self.features]
        
        plt.figure(figsize=(10, 5))
        scatter = plt.scatter(self.retention_times, mz_values, c=intensities, cmap="viridis", marker='o')
        plt.colorbar(scatter, label="Intensity")
        plt.xlabel("Retention Time / Index")
        plt.ylabel("m/z")
        plt.title("Ion Map (m/z vs Retention Time)")
        plt.show()
