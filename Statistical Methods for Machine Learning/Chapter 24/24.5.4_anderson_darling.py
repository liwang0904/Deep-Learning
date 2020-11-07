from numpy.random import seed
from numpy.random import randn
from scipy.stats import anderson

seed(1)

data = 5 * randn(100) + 50

result = anderson(data)
# Statistic: 0.220
print('Statistic: %.3f' % result.statistic)
p = 0
# 15.000: 0.555, data looks normal (fail to reject H0)
# 10.000: 0.632, data looks normal (fail to reject H0)
# 5.000: 0.759, data looks normal (fail to reject H0)
# 2.500: 0.885, data looks normal (fail to reject H0)
# 1.000: 1.053, data looks normal (fail to reject H0)
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < result.critical_values[i]:
		print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
	else:
		print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
