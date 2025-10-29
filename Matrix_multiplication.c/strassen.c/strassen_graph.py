import matplotlib.pyplot as plt

# Data
original_sizes = [101, 200, 305, 400, 509]
used_sizes = [102, 200, 306, 400, 510]
times = [0.013, 0.094, 0.221, 0.315, 0.619]

# Plot
plt.figure(figsize=(8,6))
plt.plot(used_sizes, times, marker='o', linestyle='-', linewidth=2)

# Labels and title
plt.xlabel("Matrix Size (after padding)", fontsize=12)
plt.ylabel("Execution Time (seconds)", fontsize=12)
plt.title("Strassen Matrix Multiplication Execution Time", fontsize=14)
plt.grid(True)

# Show values on points
for i in range(len(used_sizes)):
    plt.text(used_sizes[i], times[i] + 0.01, f"{times[i]:.3f}", ha='center')

plt.show()
