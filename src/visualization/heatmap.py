# src/visualization/heatmap.py
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class HeatmapVisualizer:
    def __init__(self, feature_matrix):
        """
        Initializes the HeatmapVisualizer with a feature matrix.
        
        Parameters:
        - feature_matrix (2D array): Matrix where rows are features and columns are samples/time points.
        """
        self.feature_matrix = feature_matrix

    def plot_heatmap(self):
        """
        Plots a heatmap for feature intensities.
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.feature_matrix, cmap="YlGnBu", annot=True, fmt=".1f", cbar=True)
        plt.xlabel("Sample/Time Point")
        plt.ylabel("Feature")
        plt.title("Feature Intensity Heatmap")
        plt.show()
