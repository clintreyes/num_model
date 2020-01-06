import random

sum = 0
while sum <= 21:
	a = random.randint(0,10)
	print('you have drawn %d' %a)
	sum = sum + a
	print(sum)
	if sum != 0 and sum <21:
		ans = input('would you like to draw another card? (y/n): ')
		if ans == 'y':
			continue
		else:
			break
#print(sum)