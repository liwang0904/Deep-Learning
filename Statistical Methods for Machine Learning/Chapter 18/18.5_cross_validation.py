from numpy import array
from sklearn.model_selection import KFold

data = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

kfold = KFold(3, True, 1)

# train: [0.1 0.4 0.5 0.6], test: [0.2 0.3]
# train: [0.2 0.3 0.4 0.6], test: [0.1 0.5]
# train: [0.1 0.2 0.3 0.5], test: [0.4 0.6]
for train, test in kfold.split(data):
	print('train: %s, test: %s' % (data[train], data[test]))
