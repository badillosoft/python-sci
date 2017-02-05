def f(x):
    return 2 * x ** 2 - x

X = [5, 7, 8, 9, 18, 25]

archivo = open("datos_gen.csv", "w")

for x in X:
    y = f(x)
    archivo.write("%f, %f\n" %(x, y))

archivo.close()