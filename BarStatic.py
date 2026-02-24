import matplotlib.pyplot as plt

n = int(input("How many categories? "))

categories = []
values = []

for i in range(n):
    name = input(f"Enter category {i+1}: ")
    value = int(input(f"Enter value for {name}: "))
    categories.append(name)
    values.append(value)

plt.bar(categories, values)
plt.title("Static Bar Chart (User Input)")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
