from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

seed(1)

data = 5 * randn(100) + 50

# mean=50.303 stdv=4.426
print('mean=%.3f stdv=%.3f' % (mean(data), std(data)))
