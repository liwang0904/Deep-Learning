from numpy import diag
from numpy.linalg import inv
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

Q = vectors

R = inv(Q)

L = diag(values)

B = Q.dot(L).dot(R)
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
print(B)
