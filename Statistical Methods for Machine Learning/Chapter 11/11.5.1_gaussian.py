from scipy.stats import norm

p = 0.95

value = norm.ppf(p)
# 1.6448536269514722
print(value)

p = norm.cdf(value)
# 0.95
print(p)
