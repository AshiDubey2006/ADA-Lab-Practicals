import matplotlib.pyplot as plt

# Data from your runs
n = [10000,  30000, 40000, 50000,
      70000, 80000, 90000, 100000]

time_taken = [0.000053, 0.000055, 0.000058, 0.000059,
               0.000063, 0.000063, 0.000063, 0.000063]

# Plot
plt.figure(figsize=(8,5))
plt.plot(n, time_taken, marker='o', linestyle='-', color='b', label="Binary Search")

# Labels and title
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Binary Search Time Analysis (averaged over 5 runs)")
plt.grid(True)
plt.legend()

# Save the graph as PNG
plt.savefig("binary_search_time_avg.png", dpi=300)

# Show the graph
plt.show()

