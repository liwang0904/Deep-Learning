from numpy.random import randn
from numpy.random import seed
from scipy.stats import linregress
from matplotlib import pyplot

seed(1)

x = 20 * randn(1000) + 100
y = x + (10 * randn(1000) + 50)

b1, b0, r_value, p_value, std_err = linregress(x, y)
# b0=1.011, b1=49.117
print('b0=%.3f, b1=%.3f' % (b1, b0))

yhat = b0 + b1 * x

pyplot.scatter(x, y)
pyplot.plot(x, yhat, color='r')
pyplot.show()
