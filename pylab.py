from matplotlib.pylab import *
from numpy import linspace

x = linspace(-3, 3, 30)
y = x**2
plot(x, y, 'r.')
show()