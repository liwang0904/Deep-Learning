from numpy import array
from numpy import cov

X = array([
	[1, 5, 8],
	[3, 5, 11],
	[2, 4, 9],
	[3, 6, 10],
	[1, 5, 10]])
# [[ 1  5  8]
#  [ 3  5 11]
#  [ 2  4  9]
#  [ 3  6 10]
#  [ 1  5 10]]
print(X)

Sigma = cov(X.T)
# [[1.   0.25 0.75]
#  [0.25 0.5  0.25]
#  [0.75 0.25 1.3 ]]
print(Sigma)
