import matplotlib.pyplot as plt
import numpy as np

min_val = int(input("Enter minimum value: "))
max_val = int(input("Enter maximum value: "))
num_points = int(input("How many data points? "))
num_bins = int(input("How many bins? "))
pause_time = float(input("Pause time (seconds): "))

if max_val <= min_val:
    print("Maximum must be greater than minimum!")
    exit()

plt.ion()
fig, ax = plt.subplots()

data = []

for i in range(num_points):
    new_value = np.random.randint(min_val, max_val)
    data.append(new_value)

    ax.clear()
    ax.hist(data, bins=num_bins, edgecolor='black')
    ax.set_title("Dynamic Histogram (User Controlled)")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    plt.pause(pause_time)

plt.ioff()
plt.show()
