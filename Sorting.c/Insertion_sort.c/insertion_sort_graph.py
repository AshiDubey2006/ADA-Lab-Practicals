import matplotlib.pyplot as plt

n_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

time_values = [0.002600, 0.005780, 0.013410, 0.022930, 0.036750,
               0.055330, 0.074970, 0.103680, 0.127820]

plt.figure(figsize=(10, 6))
plt.plot(n_values, time_values, marker='o', linestyle='-', color='red', label='Insertion Sort')

plt.title('Insertion Sort Execution Time vs Input Size')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
