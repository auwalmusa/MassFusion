# src/preprocessing/peak_detection.py
from scipy.signal import find_peaks

class PeakDetector:
    def __init__(self, data):
        """
        Initializes the PeakDetector with data.
        
        Parameters:
        - data: The baseline-corrected signal data.
        """
        self.data = data

    def detect_peaks(self, height=None, distance=5):
        """
        Detects peaks in the signal data.
        
        Parameters:
        - height (float): Minimum height of peaks to detect.
        - distance (int): Minimum number of samples between peaks.
        
        Returns:
        - peaks (list): Indices of detected peaks.
        - properties (dict): Properties of each detected peak.
        """
        peaks, properties = find_peaks(self.data, height=height, distance=distance)
        return peaks, properties
