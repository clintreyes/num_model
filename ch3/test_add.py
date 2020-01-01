def add(a,b):
	return a + b

def test_add():
	expected = 1 + 1
	computed = add(1,1)
	assert computed == expected, '1+1=%g' % computed

def test_add_float():
	expected = 0.3
	computed = add(0.1,0.2)
	tol = 1E-14
	diff = abs(expected - computed)
	assert diff < tol, 'diff=%g' % diff
	
# run py.test -s -v 
# or nosetests -s -v