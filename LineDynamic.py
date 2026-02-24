import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  

x_data = []
y_data = []

for i in range(20):
    x_data.append(i)
    y_data.append(np.random.randint(0, 50))

    plt.clf() 
    plt.plot(x_data, y_data, marker='o')
    plt.title("Dynamic Line Chart")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid(True)

    plt.pause(0.5)

plt.ioff()
plt.show()
