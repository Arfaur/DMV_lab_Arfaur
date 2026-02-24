import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 15, 8, 12, 20]

plt.plot(x, y, marker='o')
plt.title("Static Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
