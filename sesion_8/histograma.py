import matplotlib.pyplot as plt

def add(X, w):
    return [x + w for x in X]

w = 0.4

x1 = [1, 2, 3, 4, 5]
x2 = add(x1, w)

y1 = [10, 20, 30, 40, 50]
y2 = [50, 40, 30, 20, 10]

plt.bar(x1, y1, w)
plt.bar(x2, y2, w)

plt.show()