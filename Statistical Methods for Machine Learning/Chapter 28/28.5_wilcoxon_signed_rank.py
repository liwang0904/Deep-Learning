from numpy.random import seed
from numpy.random import rand
from scipy.stats import wilcoxon

seed(1)

data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)

stat, p = wilcoxon(data1, data2)
# Statistics=1937.000, p=0.043
print('Statistics=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
# Different distribution (reject H0)
if p > alpha:
	print('Same distribution (fail to reject H0)')
else:
	print('Different distribution (reject H0)')
