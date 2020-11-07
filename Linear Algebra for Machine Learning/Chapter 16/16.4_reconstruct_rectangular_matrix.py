from numpy import array
from numpy import diag
from numpy import zeros
from scipy.linalg import svd

A = array([
	[1, 2],
	[3, 4],
	[5, 6]])
# [[1 2]
#  [3 4]
#  [5 6]]
print(A)

U, s, VT = svd(A)

Sigma = zeros((A.shape[0], A.shape[1]))

Sigma[:A.shape[1], :A.shape[1]] = diag(s)

B = U.dot(Sigma.dot(VT))
# [[1. 2.]
#  [3. 4.]
#  [5. 6.]]
print(B)
