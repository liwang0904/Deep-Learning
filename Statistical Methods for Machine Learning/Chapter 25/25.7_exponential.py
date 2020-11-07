from numpy.random import seed
from numpy.random import randn
from numpy import exp
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 50

data = exp(data)

pyplot.hist(data)
pyplot.show()
