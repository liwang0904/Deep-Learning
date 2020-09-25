from numpy import array

A = array([[1, 2], [3, 4], [5, 6]])
# [[1 2]
#  [3 4]
#  [5 6]]
print(A)

b = 0.5
# 0.5
print(b)

C = A * b
# [[0.5 1. ]
#  [1.5 2. ]
#  [2.5 3. ]]
print(C)
