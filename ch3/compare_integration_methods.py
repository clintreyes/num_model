from trapezoidal import trapezoidal
from midpoint import midpoint
from math import exp
from sympy import *

t = symbols('t')
v = 3*t**2*exp(t**3)
V = integrate(v,t)
#print(V)

g = lambda y: 3*y**2*exp(y**3)
a = 0.0
b = 1.0
exact = V.subs(t,b) - V.subs(t,a)
print(exact)

print('	n	midpoint	rel error	trapezoidal	rel error')
for i in range(1,10):
	n = 2**i
	m = midpoint(g,a,b,n)
	t = trapezoidal(g,a,b,n)
	print('%7d	%.16f	%.4f	%.16f	%.4f' \
		%(n,m,(exact-m)/exact*100,t,(exact-t)/exact*100))