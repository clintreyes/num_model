import numpy as np
import matplotlib.pyplot as plt
import math

N = int(input("Input number of terms for pi, N:"))
sum = 0
a = np.zeros(N)
x = np.arange(0,N,1)
e = np.zeros(N)

for k in range(1,N+1):
	sum += 1/k**2
	a[k-1] = math.sqrt(6*sum)
	e[k-1] = abs(a[k-1]-math.pi)
print(a)

fig, axs = plt.subplots(2)

axs[0].plot(x,a)
axs[0].set_title('pi value')
axs[1].plot(x,e)
axs[1].set_title('error')

plt.show()
