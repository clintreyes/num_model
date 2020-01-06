def average_integer(N):
	sum = 0
	for i in range(0,N+1):
		sum += i
	return sum

N = int(input("input an integer: "))
print(average_integer(N))