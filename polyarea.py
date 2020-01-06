def polyarea(x,y):
	sum = 0
	for i in range(0,len(x)):
		if i == len(x)-1:
			sum += x[len(x)-1]*y[0] - y[len(x)-1]*x[0]
		else:
			sum += x[i]*y[i+1] - y[i]*x[i+1]
	return 0.5*sum

x = [1,2,3,3.5,4]
y = [1,4,1,5,2.5]
print(polyarea(x,y))