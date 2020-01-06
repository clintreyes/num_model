
def y(t):
	v0 = 5
	g = 9.81
	return v0*t - 0.5*g*t**2
time = 0.6
h = y()
print(h)
time = 0.9
h = y(time)
print(h)

def check_sign(x):
	if x > 0:
		return 'x is positive'
	elif x < 0:
		return 'x is negative'
	else:
		return 'x is zero'
