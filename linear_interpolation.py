'''
	Solves linear interpolation
	yi from 1 to N
	ti = i to N
'''
import numpy as np

def find(y,time):
	t = np.arange(0.0,len(y))
	i = 0
	while time > t[i]:
		i = i + 1
	i = i - 1 

	yt = (y[i+1] - y[i]) / (t[i+1] - t[i]) * (time - t[i]) + y[i]
	return yt

#y = np.linspace(1,10,4)
y = np.array([4.4,2.0,11.0,21.5,7.5])
t = np.arange(0.0,len(y))

#	user input time
#time = float(input('user input time, t: '))
#while time < 0:
#	time = float(input('error input a positive time, t: '))

yt = find(y,2.5)
print(yt)

yt2 = find(y,3.1)
print(yt2)

#plot for check only
import matplotlib.pyplot as plt

ax = plt.plot(t,y)
plt.show()
