import matplotlib.pyplot as plt
import numpy as np


x_min = int(input("Enter X-axis minimum: "))
x_max = int(input("Enter X-axis maximum: "))
y_min = int(input("Enter Y-axis minimum: "))
y_max = int(input("Enter Y-axis maximum: "))
num_points = int(input("How many points to plot? "))
pause_time = float(input("Pause time between updates (seconds): "))

plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_title("Animated Line Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.grid(True)

x_data = []
y_data = []


for i in range(num_points):
    x_new = np.random.randint(x_min, x_max)
    y_new = np.random.randint(y_min, y_max)
    
    x_data.append(x_new)
    y_data.append(y_new)
    
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title("Animated Line Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.grid(True)
    
    ax.plot(x_data, y_data, color='blue', marker='o', linestyle='-', linewidth=2)
    
    plt.pause(pause_time)

plt.ioff()
plt.show()
