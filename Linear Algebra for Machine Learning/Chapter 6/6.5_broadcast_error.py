from numpy import array

A = array([[1, 2, 3], [1, 2, 3]])
# (2, 3)
print(A.shape)

b = array([1, 2])
# (2,)
print(b.shape)

C = A + b
# ValueError: operands could not be broadcast together with shapes (2,3) (2,)
print(C)
