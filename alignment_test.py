import numpy as np
import matplotlib.pyplot as plt
from src.preprocessing.alignment import Aligner

# Create synthetic data
reference_data = np.sin(np.linspace(0, 10, 100))
sample_data = np.roll(reference_data, 5)  # Shift sample data by 5 indices

# Initialize Aligner
aligner = Aligner(reference_data, sample_data)
aligned_data, shift_index = aligner.align()

# Print results
print("Shift Index:", shift_index)

# Visualize to check alignment
plt.figure(figsize=(10, 5))
plt.plot(reference_data, label='Reference Data', color='blue')
plt.plot(sample_data, label='Original Sample Data (shifted)', color='red', linestyle='--')
plt.plot(aligned_data, label='Aligned Sample Data', color='green', linestyle=':')
plt.legend()
plt.title("Alignment Check")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
