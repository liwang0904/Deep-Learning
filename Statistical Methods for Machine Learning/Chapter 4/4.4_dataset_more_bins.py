from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

data = 5 * randn(10000) + 50

pyplot.hist(data, bins=100)
pyplot.show()
