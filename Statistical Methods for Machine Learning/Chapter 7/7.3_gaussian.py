from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm

xaxis = arange(30, 70, 1)

yaxis = norm.pdf(xaxis, 50, 5)

pyplot.plot(xaxis, yaxis)
pyplot.show()
