from random import *

a = [0] * 6
for i in range(0,len(a)):
	a[i] = uniform(0,10)
	print(a[i])

a.sort()
print(a)
