from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm

x_axis = arange(-3, 3, 0.001)

pyplot.plot(x_axis, norm.pdf(x_axis, 0, 0.5))

pyplot.plot(x_axis, norm.pdf(x_axis, 0, 1))
pyplot.show()
