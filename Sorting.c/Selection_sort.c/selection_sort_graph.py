import matplotlib.pyplot as plt



# Input sizes
n_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

# Corresponding execution times
time_values = [0.003830, 0.017780, 0.030200, 0.040640, 0.067070,
               0.098420, 0.132590, 0.160940, 0.204430]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(n_values, time_values, marker='o', linestyle='-', color='blue', label='Selection Sort')

# Adding labels and title
plt.title('Selection Sort Time Complexity')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
