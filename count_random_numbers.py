import random

N = int(input("Input positive integer, N: "))
a = [0]*N
M = 0

for i in range(0,N):
	a[i] = random.randint(1,6)
	if a[i] == 6:
		M += 1
print(M)