from numpy.random import seed
from numpy.random import randn
from numpy import std

seed(1)

data = 5 * randn(10000) + 50

result = std(data)
# Standard Deviation: 4.994
print('Standard Deviation: %.3f' % result)
