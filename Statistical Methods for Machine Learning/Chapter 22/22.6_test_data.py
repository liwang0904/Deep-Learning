from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot

seed(1)

x = 20 * randn(1000) + 100
y = x + (10 * randn(1000) + 50)

# x: mean=100.776 stdv=19.620
print('x: mean=%.3f stdv=%.3f' % (mean(x), std(x)))
# y: mean=151.050 stdv=22.358
print('y: mean=%.3f stdv=%.3f' % (mean(y), std(y)))

pyplot.scatter(x, y)
pyplot.show()
