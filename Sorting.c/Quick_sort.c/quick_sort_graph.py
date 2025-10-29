import matplotlib.pyplot as plt

# Quick Sort data
n_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
time_values = [0.000160, 0.000410, 0.000650, 0.000890, 0.001100,
               0.001360, 0.001620, 0.001940, 0.002140, 0.002440]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(n_values, time_values, marker='o', linestyle='-', color='blue', label='Quick Sort')

# Title and labels
plt.title('Quick Sort Execution Time vs Input Size')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
