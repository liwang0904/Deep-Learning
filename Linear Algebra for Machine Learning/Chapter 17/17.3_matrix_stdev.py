from numpy import array
from numpy import std

M = array([
	[1,2,3,4,5,6],
	[1,2,3,4,5,6]])
# [[1 2 3 4 5 6]
#  [1 2 3 4 5 6]]
print(M)

col_std = std(M, ddof=1, axis=0)
# [0. 0. 0. 0. 0. 0.]
print(col_std)

row_std = std(M, ddof=1, axis=1)
# [1.87082869 1.87082869]
print(row_std)
