from numpy import array
from numpy import tensordot

A = array([1,2])

B = array([3,4])

C = tensordot(A, B, axes=0)
# [[3 4]
#  [6 8]]
print(C)
