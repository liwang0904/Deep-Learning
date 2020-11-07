from numpy import array
from numpy.linalg import svd
from numpy import zeros
from numpy import diag

A = array([
	[0.1, 0.2],
	[0.3, 0.4],
	[0.5, 0.6],
	[0.7, 0.8]])
# [[0.1 0.2]
#  [0.3 0.4]
#  [0.5 0.6]
#  [0.7 0.8]]
print(A)

U, s, VT = svd(A)

d = 1.0 / s

D = zeros(A.shape)

D[:A.shape[1], :A.shape[1]] = diag(d)

B = VT.T.dot(D.T).dot(U.T)
# [[-1.00000000e+01 -5.00000000e+00  9.07607323e-15  5.00000000e+00]
#  [ 8.50000000e+00  4.50000000e+00  5.00000000e-01 -3.50000000e+00]]
print(B)
