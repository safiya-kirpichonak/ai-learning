import numpy

# vector 1
a = numpy.array([0, 1, 2, 3])

# vector 2
b = numpy.array([4, 5, 6, 7])

# matrix
c = numpy.array([[0, 1, 2, 3], [4, 5, 6, 7]])

# matrix with zeros 2x4
d = numpy.zeros((2, 4))

# matrix with random numbers from 0 - 1 2x5
e = numpy.random.rand(2, 5)

print(a)
print(b)
print(c)
print(d)
print(e)

# [0.0 0.1 0.2 0.3] (a[i] * 0.1)
print(a * 0.1)

# [[0.0 0.2 0.4 0.6] [0.8 1.0 1.2 1.4]] (c[i][j] * 0.2)
print(c * 0.2)

# [0 5 12 21] (a[i] * b[i])
print(a * b)

# [0.0 1.0 2.4 4.2] (a[i] * b[i] * 0.2)
print(a * b * 0.2)

# [[0 1 4 9] [0 5 12 21]] (a[i] * c[i][j])
print(a * c)

# ValueError: operands could not be broadcast together with shapes (4) (2,5); 1x4 * 2x5
# print(a * e)

a2 = numpy.zeros((1, 4))
b2 = numpy.zeros((4, 3))

# (1, 4) dot (4, 3) => (1, 3), because IxJ dot MxN J == M => IxN; 
# if J != M => error
c2 = a2.dot(b2)
print(c2.shape)

# T = transform: 5x4 => 4x5
h = numpy.zeros((5, 4)).T
i = numpy.zeros((5, 6))
j = h.dot(i)
print(j.shape) # (4, 6)

# ValueError: shapes (5,4) and (5,6) not aligned: 4 (dim 1) != 5 (dim 0)
m = numpy.zeros((5, 4))
n = numpy.zeros((5, 6))
# j = m.dot(n)