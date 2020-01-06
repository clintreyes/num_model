from sympy import *
x,y = symbols('x y')

print( 2*x + 3*x - y )
print( diff(x**2, x) )
print( integrate(cos(x),x) )
print( simplify( (x**2 + x**3)/x**2 ) )
print( limit( sin(x)/x , x, 0) )
print( solve(5*x - 15, x))