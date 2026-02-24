import matplotlib.pyplot as plt
import numpy as np


num_categories = int(input("Enter number of categories: "))
categories = []

for i in range(num_categories):
    name = input(f"Enter name for category {i+1}: ")
    categories.append(name)

min_val = int(input("Enter minimum value: "))
max_val = int(input("Enter maximum value: "))
num_updates = int(input("How many updates? "))
pause_time = float(input("Pause time (seconds): "))

if max_val <= min_val:
    print("Maximum must be greater than minimum!")
    exit()

plt.ion()
fig, ax = plt.subplots()

for _ in range(num_updates):
    values = np.random.randint(min_val, max_val, len(categories))

    ax.clear()
    ax.bar(categories, values)
    ax.set_title("Dynamic Bar Chart (User Controlled)")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")

    plt.draw()
    plt.pause(pause_time)

plt.ioff()
plt.show()
