from numpy import array
from numpy import diag
from scipy.linalg import svd

A = array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(A)

U, s, VT = svd(A)

Sigma = diag(s)

B = U.dot(Sigma.dot(VT))
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
print(B)
