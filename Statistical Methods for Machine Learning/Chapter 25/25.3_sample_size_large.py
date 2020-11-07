from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

data = 50 * randn(100) + 100

pyplot.hist(data)
pyplot.show()
