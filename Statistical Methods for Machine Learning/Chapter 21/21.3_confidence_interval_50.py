from math import sqrt

interval = 1.96 * sqrt( (0.2 * (1 - 0.2)) / 50)
# 0.111
print('%.3f' % interval)
