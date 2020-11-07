from numpy import array
from numpy.linalg import cholesky

A = array([
	[2, 1, 1],
	[1, 2, 1],
	[1, 1, 2]])
# [[2 1 1]
#  [1 2 1]
#  [1 1 2]]
print(A)

L = cholesky(A)
# [[1.41421356 0.         0.        ]
#  [0.70710678 1.22474487 0.        ]
#  [0.70710678 0.40824829 1.15470054]]
print(L)

B = L.dot(L.T)
# [[2. 1. 1.]
#  [1. 2. 1.]
#  [1. 1. 2.]]
print(B)
