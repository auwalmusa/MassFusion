# src/preprocessing/noise_reduction.py
import numpy as np
from scipy.signal import savgol_filter

class NoiseReducer:
    def __init__(self, data):
        """
        Initializes the NoiseReducer with data.
        
        Parameters:
        - data: The raw signal data to be processed.
        """
        self.data = data

    def apply_savgol_filter(self, window_length=11, polyorder=2):
        """
        Applies a Savitzky-Golay filter to smooth the signal data.
        
        Parameters:
        - window_length (int): Length of the filter window (odd number).
        - polyorder (int): Polynomial order for the filter.
        
        Returns:
        - Smoothed data array.
        """
        smoothed_data = savgol_filter(self.data, window_length=window_length, polyorder=polyorder)
        return smoothed_data
