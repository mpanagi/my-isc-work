import numpy as np
import numpy.ma as MA

# arrays in different ways
'''
a = np.zeros((2,3,4))
b = np.ones((2,3,4))
c = np.arange(1000)

print a
print b
print c
'''

#interogating an array
'''
arr = np.array([range(4), range(10, 14)])

print arr.shape

print arr.size

print arr.max()

print arr.min()
'''

# generating new arrays by modifying the old one
'''
arr = np.array([range(4), range(10, 14)])

print np.reshape(arr, (2, 2, 2))

print np.transpose(arr)

print np.ravel(arr)

print arr.astype(np.float64)
'''

# array calculations
'''
a = np.array([range(4), range(10, 14)])
b = np.array([2, -1, 1, 0])

c = a * b
print c

b1 = b * 100
print b1

b2 = b * 100.0
print b2

print b1 == b2

print b1.dtype, b2.dtype
'''

# array comparison
'''
arr = np.arange(10)
print arr

print arr < 3 
print np.less(arr, 3)

condition = np.logical_or(arr < 3, arr > 8)
print condition

new_arr = np.where(condition, arr *5, arr * -5)
print new_arr
'''

# implement a mathimatical function that works on arrays
'''
def magnitude(u, v, min = 0.1):
	magn = np.sqrt(u**2 + v**2)
	
# NEED TO FINISH THIS #
'''

# create a masked array
'''
marr = MA.masked_array(range(10), fill_value = -999)
print marr, marr.fill_value

marr[2] = MA.masked
print marr
print marr.mask

narr = MA.masked_where(marr > 6, marr)
print narr

x = MA.filled(narr)
print x

print type(x)
'''

# create a mask that is smaller than the overall array

m1 = MA.masked_array(range(1, 9))
print m1

m2 = m1.reshape(2,4)
print m2

m3 = MA.masked_greater(m2, 6)
print m3

m4 = m3 * 100
print m4

sub = m3 - np.ones((2, 4))
print sub

print type(sub)
