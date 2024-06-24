import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

print(x)
print(y)
print(z)

# sin wave
plt.plot(x, y)
plt.show()

# cos wave
plt.plot(x, z)
plt.show()

# add title to x-axis and y-axis
plt.plot(x, y)
plt.xlabel('angle')
plt.ylabel('sin')
plt.title('Sin wave')
plt.show()

# parabola
x = np.linspace(-10, 10, 20)
y = x**2

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'r+') # red + symbol
plt.show()

plt.plot(x, y, 'g.') # green dot
plt.show()

plt.plot(x, y, 'rx')
plt.show()

x = np.linspace(-5, 5, 50)

plt.plot(x, np.sin(x), 'g-')
plt.plot(x, np.cos(x), 'r--')
plt.show()

# Bar plot
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 12]
ax.bar(langs, students)
plt.xlabel('Languages')
plt.ylabel('No of students')
plt.show()

# Pie chart
fig1 = plt.figure()
ax = fig1.add_axes([0, 0, 1, 1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 12]
ax.pie(students, labels=langs, autopct='%1.2f%%')
plt.show()

# Scatter plot
x = np.linspace(0, 10, 30)
y = np.sin(x)
z = np.cos(x)

fig1 = plt.figure()
ax = fig1.add_axes([0, 0, 1, 1])
ax.scatter(x, y, color='g')
ax.scatter(x, z, color='r')
plt.show()

# 3D scatter plot
fig1 = plt.figure()
ax = plt.axes(projection='3d')
z = 20 * np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x, y, z, c = z, cmap='Blues')
plt.show()