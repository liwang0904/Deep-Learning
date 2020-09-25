from numpy import array
from numpy import tril
from numpy import triu

M = array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]
print(M)

lower = tril(M)
# [[1 0 0]
#  [1 2 0]
#  [1 2 3]]
print(lower)

upper = triu(M)
# [[1 2 3]
#  [0 2 3]
#  [0 0 3]]
print(upper)
