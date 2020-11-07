from statsmodels.stats.power import TTestIndPower

effect = 0.8
alpha = 0.05
power = 0.8

analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
# Sample Size: 25.525
print('Sample Size: %.3f' % result)
