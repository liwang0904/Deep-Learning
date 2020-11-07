from numpy import array
from numpy.linalg import pinv
from matplotlib import pyplot

data = array([
	[0.05, 0.12],
	[0.18, 0.22],
	[0.31, 0.35],
	[0.42, 0.38],
	[0.5, 0.49]])

X, y = data[:,0], data[:,1]
X = X.reshape((len(X), 1))

b = pinv(X).dot(y)
# [1.00233226]
print(b)

yhat = X.dot(b)

pyplot.scatter(X, y)
pyplot.plot(X, yhat, color='red')
pyplot.show()
