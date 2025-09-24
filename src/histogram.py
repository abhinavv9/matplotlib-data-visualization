import matplotlib.pyplot as plt
import numpy as np

# --- Histogram Example ---
# Generate sample data: 1000 random numbers from a standard normal distribution
data = np.random.randn(1000)

plt.figure(figsize=(8, 6))

# Create the histogram
# 'bins' controls the number of bars. 'edgecolor' adds borders to bars.
n, bins, patches = plt.hist(data, bins=30, edgecolor='black', alpha=0.7, color='purple')

# Add Title and Axis Labels
plt.title('Histogram of Random Data Distribution', fontsize=16)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Optional: Add a vertical line for the mean
mean_value = np.mean(data)
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_value:.2f}')
plt.legend()

# Ensure layout is tight
plt.tight_layout()

# Display the plot
plt.show()
