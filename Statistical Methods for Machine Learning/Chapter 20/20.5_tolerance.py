from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import sqrt
from scipy.stats import chi2
from scipy.stats import norm

seed(1)

data = 5 * randn(100) + 50

n = len(data)
dof = n - 1

prop = 0.95
prop_inv = (1.0 - prop) / 2.0
gauss_critical = norm.ppf(prop_inv)
# Gaussian critical value: -1.960 (coverage=95%)
print('Gaussian critical value: %.3f (coverage=%d%%)' % (gauss_critical, prop*100))

prob = 0.99
prop_inv = 1.0 - prob
chi_critical = chi2.ppf(prop_inv, dof)
# Chi-Squared critical value: 69.230 (prob=99%, dof=99)
print('Chi-Squared critical value: %.3f (prob=%d%%, dof=%d)' % (chi_critical, prob*100, dof))

interval = sqrt((dof * (1 + (1/n)) * gauss_critical**2) / chi_critical)
# Tolerance Interval: 2.355
print('Tolerance Interval: %.3f' % interval)

data_mean = mean(data)
lower, upper = data_mean-interval, data_mean+interval
# 47.95 to 52.66 covers 95% of data with a confidence of 99%
print('%.2f to %.2f covers %d%% of data with a confidence of %d%%' % (lower, upper, prop*100, prob*100))
