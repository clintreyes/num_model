from matplotlib.pylab import *
import numpy as np

y = np.array([0.5,2.0,1.0,1.5,7.5])
x = np.arange(0,5)
e = np.zeros(len(y))

def error_calc(a,b,x,y):
	error = 0
	for i in range(0,len(y)):
		e[i] = (a*x[i] + b - y[i]) ** 2
		error += e[i]
	return error

#print(error_calc(a,b,x,y))

def optimize(x,y):
	error = 25
	while error > 10.0:
		a = float( input("input a: "))
		b = float( input("input b: "))
		error = error_calc(a,b,x,y)
		f = a*x + b
		print(error)
		plot(x,f)
		plot(x,y,'r.')
		show()

optimize(x,y)
#interactive, not automated