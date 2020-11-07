from numpy import array
from numpy.linalg import eig

A = array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(A)

values, vectors = eig(A)
# [ 1.61168440e+01 -1.11684397e+00 -9.75918483e-16]
print(values)
# [[-0.23197069 -0.78583024  0.40824829]
#  [-0.52532209 -0.08675134 -0.81649658]
#  [-0.8186735   0.61232756  0.40824829]]
print(vectors)
