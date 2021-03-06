from numpy import array
from scipy.linalg import lu

A = array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(A)

P, L, U = lu(A)
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]
print(P)
# [[1.         0.         0.        ]
#  [0.14285714 1.         0.        ]
#  [0.57142857 0.5        1.        ]]
print(L)
# [[ 7.00000000e+00  8.00000000e+00  9.00000000e+00]
#  [ 0.00000000e+00  8.57142857e-01  1.71428571e+00]
#  [ 0.00000000e+00  0.00000000e+00 -1.58603289e-16]]
print(U)

B = P.dot(L).dot(U)
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
print(B)
