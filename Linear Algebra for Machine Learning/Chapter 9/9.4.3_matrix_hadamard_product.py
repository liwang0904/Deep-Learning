from numpy import array

A = array([[1, 2, 3], [4, 5, 6]])
# [[1 2 3]
#  [4 5 6]]
print(A)

B = array([[1, 2, 3], [4, 5, 6]])
# [[1 2 3]
#  [4 5 6]]
print(B)

C = A * B
# [[ 1  4  9]
#  [16 25 36]]
print(C)
