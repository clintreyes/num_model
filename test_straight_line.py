from sympy import *
import random

x = symbols('x')
f = 4*x + 1

lower = 0
upper = 10
c = 2

for i in range(0,100):
	xi = random.uniform(lower,upper)
	a = ( f.subs(x, xi) - f.subs(x, c) ) / (xi - c)
	print(a)