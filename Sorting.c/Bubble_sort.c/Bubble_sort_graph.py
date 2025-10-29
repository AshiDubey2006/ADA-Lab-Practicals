import matplotlib.pyplot as plt

# Data from the screenshot
n_values = [10, 50, 100, 500, 1000, 5000, 10000]
time_values = [0.000000, 0.000020, 0.000100, 0.002080, 0.004640, 0.119040, 0.633710]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(n_values, time_values, marker='o', linestyle='-', linewidth=2, markersize=6)
plt.title("Bubble Sort: Time vs n")
plt.xlabel("n (Number of Elements)")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
