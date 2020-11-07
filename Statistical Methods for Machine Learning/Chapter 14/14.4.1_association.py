from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr

seed(1)

data1 = 10 * randn(10000) + 50
data2 = data1 + (10 * randn(10000) + 50)

corr, _ = pearsonr(data1, data2)
# Pearsons correlation: 0.712
print('Pearsons correlation: %.3f' % corr)
