from numpy import array

data = array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

X, y = data[:, :-1], data[:, -1]

# [[11 22]
#  [44 55]
#  [77 88]]
print(X)
# [33 66 99]
print(y)
