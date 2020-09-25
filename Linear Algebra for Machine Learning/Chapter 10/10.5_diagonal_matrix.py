from numpy import array
from numpy import diag

M = array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]
print(M)

d = diag(M)
# [1 2 3]
print(d)

D = diag(d)
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
print(D)
