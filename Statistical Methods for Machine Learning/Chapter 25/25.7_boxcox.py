from numpy.random import seed
from numpy.random import randn
from numpy import exp
from scipy.stats import boxcox
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 100

data = exp(data)

data = boxcox(data, 0)

pyplot.hist(data)
pyplot.show()
