from trapezoidal import trapezoidal
from midpoint import midpoint
import sympy

def integrate_parabola(f, a, b, n = 100):
	I_t = trapezoidal(f, a, b, n)
	I_m = midpoint(f, a , b, n)

	x =sympy.symbols('x')
	I_exact = sympy.integrate(f(x), (x,a,b))
	#relative error
	error_t = abs(I_exact-I_t) / I_exact *100
	error_m = abs(I_exact-I_m) / I_exact *100
	print('%d\t%f\t%.2f\t%f\t%.2f' %(n,I_t,error_t,I_m,error_m))
	return None

#def f(x):
#	return x*(x-1)

f = lambda x: x*(x-1) #same as def and return -ing the function
a = 2.0; b = 6.0

print('n\ttrapezoidal\terror(%)\tmidpoint\terror(%)')
integrate_parabola(f,a,b,100)
integrate_parabola(f,a,b,2)
