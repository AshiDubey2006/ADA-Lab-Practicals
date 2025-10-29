import matplotlib.pyplot as plt

# Data from user's program output
original_sizes = [101, 200, 305, 400, 509]
used_sizes = [102, 200, 306, 400, 510]
times = [0.019, 0.202, 0.391, 0.747, 1.504]

# Plotting
plt.figure(figsize=(7,5))
plt.plot(original_sizes, times, marker='o', linestyle='-', linewidth=2, markersize=8, label="Original size")
plt.plot(used_sizes, times, marker='s', linestyle='--', linewidth=2, markersize=6, label="Used (padded) size")

plt.title("Matrix Multiplication Execution Time with Padding", fontsize=14)
plt.xlabel("Matrix Size (n x n)", fontsize=12)
plt.ylabel("Time Taken (seconds)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
