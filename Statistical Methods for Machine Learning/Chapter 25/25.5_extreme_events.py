from numpy.random import seed
from numpy.random import randn
from numpy import zeros
from numpy import append
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 10

data = append(data, zeros(10))

pyplot.hist(data)
pyplot.show()
