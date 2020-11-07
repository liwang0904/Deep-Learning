from numpy.random import randn
from numpy.random import seed
from numpy import sqrt
from numpy import sum as arraysum
from scipy.stats import linregress
from matplotlib import pyplot

seed(1)

x = 20 * randn(1000) + 100
y = x + (10 * randn(1000) + 50)

b1, b0, r_value, p_value, std_err = linregress(x, y)

yhat = b0 + b1 * x

x_in = x[0]
y_out = y[0]
yhat_out = yhat[0]

sum_errs = arraysum((y - yhat)**2)
stdev = sqrt(1/(len(y)-2) * sum_errs)

interval = 1.96 * stdev
# Prediction Interval: 20.204
print('Prediction Interval: %.3f' % interval)
lower, upper = yhat_out - interval, yhat_out + interval
# 95% likelihood that the true value is between 162.920 and 203.328
print('95%% likelihood that the true value is between %.3f and %.3f' % (lower, upper))
# True value: 183.124
print('True value: %.3f' % yhat_out)

pyplot.scatter(x, y)
pyplot.plot(x, yhat, color='red')
pyplot.errorbar(x_in, yhat_out, yerr=interval, color='black', fmt='o')
pyplot.show()
