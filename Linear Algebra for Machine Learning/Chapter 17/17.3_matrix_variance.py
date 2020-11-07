from numpy import array
from numpy import var

M = array([
	[1,2,3,4,5,6],
	[1,2,3,4,5,6]])
# [[1 2 3 4 5 6]
#  [1 2 3 4 5 6]]
print(M)

col_var = var(M, ddof=1, axis=0)
# [0. 0. 0. 0. 0. 0.]
print(col_var)

row_var = var(M, ddof=1, axis=1)
# [3.5 3.5]
print(row_var)
