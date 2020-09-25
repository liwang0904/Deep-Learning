from numpy import array
from numpy.linalg import inv

Q = array([[1, 0], [0, -1]])
# [[ 1  0]
#  [ 0 -1]]
print(Q)

V = inv(Q)
# [[ 1  0]
#  [ 0 -1]]
print(Q.T)
# [[ 1.  0.]
#  [-0. -1.]]
print(V)

I = Q.dot(Q.T)
# [[1 0]
#  [0 1]]
print(I)
