from trapezoidal import trapezoidal
from math import exp
print(trapezoidal(lambda x: exp(-x**2), -1, 1.1, 400))
