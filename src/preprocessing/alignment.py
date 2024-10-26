# src/preprocessing/alignment.py
import numpy as np
from scipy.signal import correlate
from scipy.interpolate import interp1d

class Aligner:
    def __init__(self, reference_data, sample_data):
        """
        Initializes the Aligner with reference and sample data.
        
        Parameters:
        - reference_data: The reference data array to align other samples to.
        - sample_data: The sample data array to be aligned.
        """
        self.reference_data = reference_data
        self.sample_data = sample_data

    def align(self):
        """
        Aligns sample data to the reference data using cross-correlation with interpolation.
        
        Returns:
        - Aligned sample data (interpolated to match reference).
        - shift_index (float): Optimal shift found using interpolation.
        """
        # Step 1: Calculate cross-correlation
        correlation = correlate(self.sample_data, self.reference_data, mode='full')
        shift_index = np.argmax(correlation) - (len(self.sample_data) - 1)

        # Step 2: Apply fractional shift using interpolation
        # Create an interpolation function
        x_original = np.arange(len(self.sample_data))
        interpolator = interp1d(x_original, self.sample_data, kind='linear', fill_value="extrapolate")
        
        # Shift with a fractional index
        x_shifted = x_original - shift_index
        aligned_data = interpolator(x_shifted)
        
        return aligned_data, shift_index
