# src/preprocessing/baseline_correction.py
import numpy as np
from scipy.ndimage import minimum_filter1d

class BaselineCorrector:
    def __init__(self, data):
        """
        Initializes the BaselineCorrector with data.
        
        Parameters:
        - data: The raw signal data to be processed.
        """
        self.data = data

    def rolling_baseline(self, window_size=50):
        """
        Applies a rolling minimum baseline correction.
        
        Parameters:
        - window_size (int): Size of the rolling window.
        
        Returns:
        - Baseline-corrected data array.
        """
        # Apply a rolling minimum filter to approximate the baseline
        baseline = minimum_filter1d(self.data, size=window_size)
        corrected_data = self.data - baseline
        return corrected_data
