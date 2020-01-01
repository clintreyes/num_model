from test_add import add

def test_add():
	expected = 0.3
	computed = add(0.1,0.2)
	tol = 1E-14
	diff = abs(expected - computed)
	assert diff < tol, 'diff=%g' % diff