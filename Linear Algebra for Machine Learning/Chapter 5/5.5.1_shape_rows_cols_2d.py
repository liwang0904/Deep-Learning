from numpy import array

data = [[11, 22], [33, 44], [55, 66]]
data = array(data)

# Rows: 3
print('Rows: %d' % data.shape[0])
# Cols: 2
print('Cols: %d' % data.shape[1])
