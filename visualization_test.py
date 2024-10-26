# visualization_test.py
import numpy as np
from src.visualization.plot_manager import PlotManager
from src.visualization.heatmap import HeatmapVisualizer
from src.visualization.ion_maps import IonMap

# Sample data and detected features
data = [0, 0.1, 0.2, 0.4, 0.9, 1.2, 0.8, 0.2, 0.1, 0]  # Sample signal data
features = [{"m/z": 100.1, "intensity": 0.9}, {"m/z": 150.5, "intensity": 1.2}, {"m/z": 200.3, "intensity": 0.8}]
feature_matrix = np.array([[0.5, 0.7, 0.2], [1.2, 0.9, 0.8], [0.3, 0.6, 1.1]])  # Heatmap data
retention_times = np.linspace(1, 10, len(features))

# Step 1: Chromatogram and Mass Spectrum Plotting
plot_manager = PlotManager(data)
plot_manager.plot_chromatogram()
plot_manager.plot_mass_spectrum(features)

# Step 2: Heatmap Visualization
heatmap_visualizer = HeatmapVisualizer(feature_matrix)
heatmap_visualizer.plot_heatmap()

# Step 3: Ion Map
ion_map = IonMap(features, retention_times)
ion_map.plot_ion_map()
