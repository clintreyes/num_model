import numpy as np
import math

b = np.array([4,-3])
t = np.array([-math.pi/2,math.pi/4])

def sinesum(t,b,N=len(b)):
	sn = 0
	for i in range(0,N):
		sn += b[i]*math.sin((i+1)*t[i])
	return sn

def test_sinesum():
	b = np.array([4,-3])
	t = np.array([-math.pi/2,math.pi/4])
	return sinesum(t,b)

print(test_sinesum())
