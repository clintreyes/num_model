import numpy as np

def a():
	rank = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
	suit = ['C','D','H','S']
	a = [0]*len(rank)*len(suit)

	for i in rank:
		for j in suit:
			print("%s%s" %(i,j))

def b():
	let = ['A','B','C','D','E','F','G','H','I','J','K','L','M'\
	,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	dig = ['0','1','2','3','4','5','6','7','8','9']
#	a = [ [ [ [ [" "]*len(let)]*len(let) ] * len(dig) ] *len(dig) ] *len(dig)
	a = [""]*len(let)**2*len(dig)**3
	n = 0

	while n < len(a):
		for i in let:
			for j in let: 
				for k in dig:
					for l in dig:
						for m in dig:
								a[n] = i+j+k+l+m
								n += 1
	return(a)

#a = b()
#filename = 'combine_sets_b.dat'
#outfile = open(filename,'w')
#outfile.write('#all combinations possible:\n')
#for i in a:
#	outfile.write('%s\n' %i)
#outfile.close

def c():
	die = [1,2,3,4,5,6]
	n = 0
	for i in die:
		for j in die:
			if i + j == 7:
				n += 1
	return(n)