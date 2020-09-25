from numpy import array

A = array([[1, 2, 3], [1, 2, 3]])
# [[1 2 3]
#  [1 2 3]]
print(A)

b = array([1, 2, 3])
# [1 2 3]
print(b)

C = A + b
# [[2 4 6]
#  [2 4 6]]
print(C)
