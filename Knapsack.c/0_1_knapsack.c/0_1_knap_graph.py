import matplotlib.pyplot as plt

# Data from your output
items = [10, 20, 30, 40, 50]
time_sec = [0.00002000, 0.00008000, 0.00019000, 0.00033000, 0.00053000]  # Time in seconds
memory_bytes = [2244, 8484, 18724, 32964, 51204]  # Memory in bytes

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(10,6))

# Plot Time on primary y-axis
color = 'tab:blue'
ax1.set_xlabel('Number of Items')
ax1.set_ylabel('Time (seconds)', color=color)
ax1.plot(items, time_sec, marker='o', linestyle='-', color=color, label='Time Complexity')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_title('0/1 Knapsack: Time and Space Complexity')

# Plot Memory on secondary y-axis
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:red'
ax2.set_ylabel('Memory (Bytes)', color=color)
ax2.plot(items, memory_bytes, marker='s', linestyle='--', color=color, label='Space Complexity')
ax2.tick_params(axis='y', labelcolor=color)

# Add legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# Show grid
ax1.grid(True)

plt.show()
