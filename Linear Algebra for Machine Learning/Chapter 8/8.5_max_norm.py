from numpy import inf
from numpy import array
from numpy.linalg import norm

a = array([1, 2, 3])
# [1 2 3]
print(a)

maxnorm = norm(a, inf)
# 3.0
print(maxnorm)
