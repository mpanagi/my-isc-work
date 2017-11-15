# simple function
'''
def double_it(number):
	return 2 * number

print double_it(5)
'''

# function to calculate the length ..
'''
def calc_hypo(a, b):
	hypo = (a**2 + b**2)**0.5
	return hypo

print calc_hypo(3, 4)
'''

# improve function above

def calc_hypo(a, b):
	if type(a) not in (float, int) and type(b) not in (float, int):
		print "Bad argument"
		return False
	if a <= 0 or b <= 0:
		print "Bad argument"
		return False
	hypo = (a**2 + b**2)**0.5
	return hypo

print calc_hypo(5, 3)
