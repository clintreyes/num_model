from midpoint import midpoint

def test_midpoint_2():
	assert (abs(midpoint(lambda x: 2*x**3, 1, 3, 100) - 40.0)) < 0.01