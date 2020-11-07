from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot

seed(1)

data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

# data1: mean=100.776 stdv=19.620
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
# data2: mean=151.050 stdv=22.358
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))

pyplot.scatter(data1, data2)
pyplot.show()
