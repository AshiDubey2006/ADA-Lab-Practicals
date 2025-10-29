import matplotlib.pyplot as plt

# New data provided by the user
n_values = [1000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
time_values = [0.000006, 0.000017, 0.000020, 0.000025,
               0.000030, 0.000035, 0.000040, 0.000045, 0.000050]

# Plotting
plt.figure(figsize=(8,5))
plt.plot(n_values, time_values, marker='o', linestyle='-', linewidth=2)
plt.xlabel("Number of elements (n)")
plt.ylabel("Time (seconds)")
plt.title("Linear Search Time vs Input Size (Improved Data)")
plt.grid(True)
plt.show()

