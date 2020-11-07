from numpy import array
from scipy.sparse import csr_matrix

A = array([[1, 0, 0, 1, 0, 0], [0, 0, 2, 0, 0, 1], [0, 0, 0, 2, 0, 0]])
# [[1 0 0 1 0 0]
#  [0 0 2 0 0 1]
#  [0 0 0 2 0 0]]
print(A)

S = csr_matrix(A)
#   (0, 0)	1
#   (0, 3)	1
#   (1, 2)	2
#   (1, 5)	1
#   (2, 3)	2
print(S)

B = S.todense()
# [[1 0 0 1 0 0]
#  [0 0 2 0 0 1]
#  [0 0 0 2 0 0]]
print(B)
