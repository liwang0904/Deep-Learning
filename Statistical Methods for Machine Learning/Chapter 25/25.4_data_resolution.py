from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

data = randn(100)

data = data.round(0)

pyplot.hist(data)
pyplot.show()
