from numpy import array
from numpy import trace

A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(A)

B = trace(A)
# 15
print(B)
