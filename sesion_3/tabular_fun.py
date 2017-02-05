def f(x):
    return 2 * x ** 2 - x

X = [5, 7, 8, 9, 18, 25]

for x in X:
    y = f(x)
    print "%f, %f" %(x, y)
