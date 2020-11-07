from numpy.random import seed
from numpy.random import randn
from numpy.random import rand
from numpy import append
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 10
tail = 10 + (rand(50) * 100)

data = append(data, tail)

pyplot.hist(data)
pyplot.show()
