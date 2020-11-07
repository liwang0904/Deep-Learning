from numpy.random import seed
from numpy.random import rand

seed(1)

data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)

# data1: min=50.001 max=59.889
print('data1: min=%.3f max=%.3f' % (min(data1), max(data1)))
# data2: min=51.126 max=60.973
print('data2: min=%.3f max=%.3f' % (min(data2), max(data2)))
