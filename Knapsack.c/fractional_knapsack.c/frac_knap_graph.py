import matplotlib.pyplot as plt

# Data from your C program output
items = [10, 50, 100, 200, 400, 800, 1600]
time_taken = [0.00000100, 0.00000400, 0.00001200, 0.00002700, 0.00005600, 0.00011400, 0.00026200]
memory = [160, 800, 1600, 3200, 6400, 12800, 25600]

# Create a figure with two y-axes (time and memory)
fig, ax1 = plt.subplots(figsize=(8, 5))

# Plot Time Complexity (O(n log n))
ax1.plot(items, time_taken, 'o-b', label="Time Complexity (O(n log n))", linewidth=2, markersize=6)
ax1.set_xlabel("Number of Items (n)")
ax1.set_ylabel("Execution Time (seconds)", color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, linestyle='--', alpha=0.6)

# Create second axis for Space Complexity
ax2 = ax1.twinx()
ax2.plot(items, memory, 's-r', label="Space Complexity (O(n))", linewidth=2, markersize=6)
ax2.set_ylabel("Memory Used (Bytes)", color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add title and legends
plt.title("Fractional Knapsack: Time vs Space Complexity", fontsize=12, weight='bold')
fig.tight_layout()
plt.show()
