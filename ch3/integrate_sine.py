from trapezoidal import trapezoidal
from midpoint import midpoint
from math import pi, sin

def integrate_sine(f, a, b, n = 2):
	I_t = trapezoidal(f, a, b, n)
	I_m = midpoint()
	return None

a = 0.0; b = pi
f = lambda x: sin(x)