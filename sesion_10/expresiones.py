from sympy import *

x = symbols("x")

expr = cos(x) * sin(x)

i = integrate(expr, x)

print latex(i)