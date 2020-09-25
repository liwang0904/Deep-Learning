from numpy import array
from numpy.linalg import inv

A = array([[1.0, 2.0], [3.0, 4.0]])
# [[1. 2.]
#  [3. 4.]]
print(A)

B = inv(A)
# [[-2.   1. ]
#  [ 1.5 -0.5]]
print(B)

I = A.dot(B)
# [[1.00000000e+00 1.11022302e-16]
#  [0.00000000e+00 1.00000000e+00]]
print(I)
