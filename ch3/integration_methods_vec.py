from numpy import linspace, sum

def midpoint(f, a, b, n):
	h = float(b-a)/n
	x = linspace(a + h/2, b - h/2, n)
	return h*sum(f(x)) 

from numpy import exp

v = lambda t: 3*t**2*exp(t**3)
a = midpoint(v, 0, 1, 10)
print('%.16f' %a)

def trapezoidal(f, a, b, n):
	h = float(b-a)/n
	x = linspace(a, b, n+1)
	s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
	return h*s