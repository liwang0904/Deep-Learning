from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

A = array([
	[1, 2],
	[3, 4],
	[5, 6]])
# [[1 2]
#  [3 4]
#  [5 6]]
print(A)

M = mean(A.T, axis=1)

C = A - M

V = cov(C.T)

values, vectors = eig(V)
# [[ 0.70710678 -0.70710678]
#  [ 0.70710678  0.70710678]]
print(vectors)
# [8. 0.]
print(values)

P = vectors.T.dot(C.T)
# [[-2.82842712  0.        ]
#  [ 0.          0.        ]
#  [ 2.82842712  0.        ]]
print(P.T)
