from trapezoidal import trapezoidal

def test_trapezoidal_1():
	v = lambda x: 2*x**3
	computed = trapezoidal(v, 1, 3, 100)
	expected = 40.0
	tol = 0.01
	assert (abs(computed-expected)) < tol
