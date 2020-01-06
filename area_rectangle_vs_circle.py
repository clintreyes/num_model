#area_rectangle_vs_circle.py
import math

a = 1.3
r = 10.6
Ac = math.pi * r**2
b = 0

while a*b < Ac:
	b+=1
print(b)
