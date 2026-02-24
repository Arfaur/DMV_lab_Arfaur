import matplotlib.pyplot as plt
import numpy as np


x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x, y, color='blue', marker='o')
plt.title("Static Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
