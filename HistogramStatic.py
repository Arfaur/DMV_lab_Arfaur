import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(0, 100, 50)

plt.hist(data, bins=10, edgecolor='black')
plt.title("Static Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
