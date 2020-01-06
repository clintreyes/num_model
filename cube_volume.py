from numpy import linspace
import matplotlib.pyplot as plt

L = linspace(1,3,3)

V = L**3

plt.plot(L,V)
plt.ylabel("volume")
plt.xlabel("length of cube")

plt.show()