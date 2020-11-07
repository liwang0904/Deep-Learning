from numpy import array
from numpy import count_nonzero

A = array([[1, 0, 0, 1, 0, 0], [0, 0, 2, 0, 0, 1], [0, 0, 0, 2, 0, 0]])
# [[1 0 0 1 0 0]
#  [0 0 2 0 0 1]
#  [0 0 0 2 0 0]]
print(A)

sparsity = 1.0 - count_nonzero(A) / A.size
# 0.7222222222222222
print(sparsity)
