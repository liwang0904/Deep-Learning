from numpy import array
from numpy.linalg import det

A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(A)

B = det(A)
# -9.51619735392994e-16
print(B)
