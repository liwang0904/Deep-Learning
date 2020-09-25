from numpy import array

A = array([[1, 2], [3, 4], [5, 6]])
# [[1 2]
#  [3 4]
#  [5 6]]
print(A)

B = array([[1, 2], [3, 4]])
# [[1 2]
#  [3 4]]
print(B)

C = A.dot(B)
# [[ 7 10]
#  [15 22]
#  [23 34]]
print(C)

D = A @ B
# [[ 7 10]
#  [15 22]
#  [23 34]]
print(D)
