from numpy import array
from numpy.linalg import norm

a = array([1, 2, 3])
# [1 2 3]
print(a)

l1 = norm(a, 1)
# 6.0
print(l1)
