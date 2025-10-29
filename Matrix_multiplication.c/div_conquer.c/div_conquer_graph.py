import matplotlib.pyplot as plt
import numpy as np

# New measured data
original_sizes = [101, 200, 305, 400, 509]
used_sizes = [102, 200, 306, 400, 510]
times = [0.015, 0.115, 0.298, 0.544, 1.089]

# Plot measured data
plt.figure(figsize=(8, 6))
plt.plot(original_sizes, times, marker='o', label="Divide & Conquer Time (s)")

# Add O(n^3) reference curve for comparison
sizes = np.linspace(100, 520, 100)
ref_curve = (sizes**3) / (200**3) * 0.115   # normalized to 200x200 time
plt.plot(sizes, ref_curve, 'r--', label="O(n^3) trend")

# Annotate data points
for i in range(len(original_sizes)):
    plt.text(original_sizes[i], times[i] + 0.03, f"{times[i]:.3f}", ha='center')

plt.xlabel("Original Matrix Size (n x n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Divide and Conquer Matrix Multiplication Execution Time")
# plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
