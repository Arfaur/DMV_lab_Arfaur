import matplotlib.pyplot as plt
import numpy as np


x_min = int(input("Enter X-axis minimum: "))
x_max = int(input("Enter X-axis maximum: "))
y_min = int(input("Enter Y-axis minimum: "))
y_max = int(input("Enter Y-axis maximum: "))
steps = int(input("How many steps to animate? "))
pause_time = float(input("Pause time between steps (seconds): "))


plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal') 
ax.grid(True)
circle_radius = (x_max - x_min) / 20  

x_pos = x_min
y_pos = y_min
dx = (x_max - x_min) / steps
dy = (y_max - y_min) / steps


for i in range(steps):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect('equal')
    ax.grid(True)
    circle = plt.Circle((x_pos, y_pos), circle_radius, color='red')
    ax.add_patch(circle)

 
    x_pos += dx
    y_pos += dy

    plt.pause(pause_time)

plt.ioff()
plt.show()
