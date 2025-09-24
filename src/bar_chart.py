import matplotlib.pyplot as plt

# --- Bar Chart Example ---
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 12]

plt.figure(figsize=(8, 6))

# Create the bar chart
plt.bar(categories, values, color=['skyblue', 'lightgreen', 'salmon', 'gold'])

# Add Title and Axis Labels
plt.title('Bar Chart Example', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Value', fontsize=12)

# Add value labels on top of each bar for clarity
for i, value in enumerate(values):
    plt.text(i, value + 1, str(value), ha='center', va='bottom', fontsize=10)

# Add grid for better readability on the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Ensure layout is tight
plt.tight_layout()

# Display the plot
plt.show()
