from numpy import array

data = [[11, 22], [33, 44], [55, 66]]
data = array(data)

# (3, 2)
print(data.shape)

# (3, 2, 1)
data = data.reshape((data.shape[0], data.shape[1], 1))

print(data.shape)
