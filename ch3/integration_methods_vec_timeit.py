from integration_methods_vec import midpoint as midpoint_vec
from midpoint import midpoint
from numpy import exp
import timeit

v = lambda t: 3*t**2*exp(t**3)

print(timeit(midpoint_vec(v, 0, 1, 1000000)))
