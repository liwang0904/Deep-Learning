from numpy import array
from numpy.linalg import matrix_rank

v1 = array([1,2,3])
# [1 2 3]
print(v1)

vr1 = matrix_rank(v1)
# 1
print(vr1)

v2 = array([0,0,0,0,0])
# [0 0 0 0 0]
print(v2)

vr2 = matrix_rank(v2)
# 0
print(vr2)
