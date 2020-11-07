from numpy.random import seed
from numpy.random import randint
from numpy import mean
from matplotlib import pyplot

seed(1)

means = [mean(randint(1, 7, 50)) for _ in range(1000)]

pyplot.hist(means)
pyplot.show()
