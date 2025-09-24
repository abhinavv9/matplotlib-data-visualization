import matplotlib.pyplot as plt
import numpy as np

# --- Step 1: Prepare Data for Scatter Plot ---
x_scatter = np.random.rand(50) * 10 # 50 random x values
y_scatter = np.random.rand(50) * 10 # 50 random y values

# Optional: Generate sizes and colors for more advanced scatter plots
sizes = np.random.rand(50) * 100  # Sizes for each point
colors = np.random.rand(50)      # Colors for each point (will be mapped to a colormap)

# --- Step 2: Create the Scatter Plot with Customizations ---
plt.figure(figsize=(8, 6))

# Basic scatter plot
# plt.scatter(x_scatter, y_scatter)

# Scatter plot with size and color variation
scatter = plt.scatter(x_scatter, y_scatter, s=sizes, c=colors, alpha=0.7, cmap='viridis')

# Add Title and Axis Labels
plt.title('Random Scatter Plot with Size and Color Variation', fontsize=16)
plt.xlabel('X Values', fontsize=12)
plt.ylabel('Y Values', fontsize=12)

# Add a colorbar for reference if using color mapping
plt.colorbar(scatter, label='Color Intensity')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure layout is tight
plt.tight_layout()

# Display the plot
plt.show()
