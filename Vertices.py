import matplotlib.pyplot as plt

n = int(input("Enter the number of vertices: "))

vertices = []

for i in range(n):
    x = float(input(f"Enter x-coordinate of vertex {i+1}: "))
    y = float(input(f"Enter y-coordinate of vertex {i+1}: "))
    vertices.append((x, y))

x_vals = [v[0] for v in vertices]
y_vals = [v[1] for v in vertices]

x_vals.append(vertices[0][0])
y_vals.append(vertices[0][1])

plt.plot(x_vals, y_vals, 'b-o') 
plt.title("User-Defined Polygon")
plt.grid(True)
plt.show()
