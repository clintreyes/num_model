import numpy as np

N = input("Number of points, N: ")
e = input("tolerance, e: ")

N = float(N)
e = float(e)

x = -4.0
n = 0.0
while n < 2:
	while abs(x-x**2) > e:
		x += 8/N
	n += 1
	print(x)
