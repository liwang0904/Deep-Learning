from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

seed(1)

data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51

# data1: mean=50.303 stdv=4.426
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
# data2: mean=51.764 stdv=4.660
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
