import numpy as np
from src.preprocessing.noise_reduction import NoiseReducer
from src.preprocessing.baseline_correction import BaselineCorrector
from src.preprocessing.peak_detection import PeakDetector

# Sample data (replace with real data for practical testing)
data = np.random.normal(0, 1, 1000) + np.sin(np.linspace(0, 10, 1000))

# Step 1: Noise Reduction
noise_reducer = NoiseReducer(data)
smoothed_data = noise_reducer.apply_savgol_filter()

# Step 2: Baseline Correction
baseline_corrector = BaselineCorrector(smoothed_data)
corrected_data = baseline_corrector.rolling_baseline()

# Step 3: Peak Detection
peak_detector = PeakDetector(corrected_data)
peaks, properties = peak_detector.detect_peaks(height=0.5)

print("Detected Peaks:", peaks)
