import matplotlib.pyplot as plt

# Merge Sort timing data
n_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
time_values = [0.000220, 0.000530, 0.000810, 0.001060, 0.001400,
               0.001710, 0.001970, 0.002330, 0.002600, 0.002910]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, time_values, marker='o', linestyle='-', color='green', label='Merge Sort')

# Add labels and title
plt.title('Merge Sort Execution Time vs Input Size')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
