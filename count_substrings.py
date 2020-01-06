gene = 'AGTCAATGGAATAGGCCAAGCGAATATTTGGGCTACCA'

def freq(letter,text):
	j = 0
	for i in text:
		if(i == letter):
			j += 1
	return j

print("The frequency of A in string gene is %d" %freq('A',gene))
print("The frequency of C in string gene is %d" %freq('C',gene))
print("The frequency of G in string gene is %d" %freq('G',gene))

def pairs(letter,text):
	j = 0
	for i in range(len(text)-1):
		if(text[i] == letter):
			if(text[i+1] == letter):
				j += 1
	return j

print(pairs('G',gene))

def mystruct(text):
	for i in range(len(text)):
		if(text[i] == )