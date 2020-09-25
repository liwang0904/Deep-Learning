from numpy import array

A = array([[1, 2, 3], [4, 5, 6]])
# [[1 2 3]
#  [4 5 6]]
print(A)

B = array([[0.5, 0.5, 0.5],	[0.5, 0.5, 0.5]])
# [[0.5 0.5 0.5]
#  [0.5 0.5 0.5]]
print(B)

C = A - B
# [[0.5 1.5 2.5]
#  [3.5 4.5 5.5]]
print(C)
