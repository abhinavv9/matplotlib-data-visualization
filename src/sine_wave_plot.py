import matplotlib.pyplot as plt
import numpy as np

# --- Step 1: Prepare Your Data ---
x = np.linspace(0, 10, 100) # 100 points from 0 to 10
y = np.sin(x)             # Calculate the sine of each x value

# --- Step 2: Create the Plot with Customizations ---
plt.figure(figsize=(8, 6)) # Optional: Adjust figure size

plt.plot(x, y, label='sin(x)', color='blue', linestyle='-') # Added color and linestyle for demonstration

# Add Title, Labels, and Legend
plt.title('Sine Wave Visualization', fontsize=16)
plt.xlabel('X-axis values', fontsize=12)
plt.ylabel('Sine(X)', fontsize=12)
plt.legend()

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure layout is tight to prevent labels overlapping
plt.tight_layout()

# Display the plot
plt.show()
