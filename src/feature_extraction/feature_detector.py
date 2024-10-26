# src/feature_extraction/feature_detector.py
import numpy as np

class FeatureDetector:
    def __init__(self, data, peaks):
        """
        Initializes the FeatureDetector with data and peak positions.
        
        Parameters:
        - data (array): Signal data from which features will be detected.
        - peaks (array): Indices of detected peaks from peak detection.
        """
        self.data = data
        self.peaks = peaks
        self.features = []

    def detect_features(self, min_intensity=0.1):
        """
        Detects molecular features based on peak intensities.
        
        Parameters:
        - min_intensity (float): Minimum intensity required to qualify as a feature.
        
        Returns:
        - features (list): List of dictionaries with m/z and intensity for each feature.
        """
        for peak in self.peaks:
            intensity = self.data[peak]
            if intensity >= min_intensity:
                feature = {"m/z": intensity, "intensity": intensity}  # Use intensity as m/z
                self.features.append(feature)
        return self.features
