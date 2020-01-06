def f(x):
	return exp(-x)*sin(x) + 5*x

from numpy import exp, sin, linspace
x = linspace(-10,10,101)
y = f(x)

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.grid()
plt.show()