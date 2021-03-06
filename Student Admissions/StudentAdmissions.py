# importing pandas and numpy
import pandas as pd
import numpy as np

# read csv file into a pd dataframe
data = pd.read_csv('student_data.csv')

# show the first 10 rows of the data
data[:10]

X = np.array(data[["gre", "gpa"]])
y = np.array(data["admit"])
    
admitted = X[np.argwhere(y==1)]
rejected = X[np.argwhere(y==0)]
rejected.shape

import matplotlib.pyplot as plt

def plot_points(data):
    X = np.array(data[["gre", "gpa"]])
    y = np.array(data["admit"])
    
    admitted = X[np.argwhere(y==1)]
    rejected = X[np.argwhere(y==0)]
    
    plt.scatter([s[0][0] for s in rejected], [s[0][1] for s in rejected], s=25, color = 'red', edgecolor = 'k')
    plt.scatter([s[0][0] for s in admitted], [s[0][1] for s in admitted], s = 25, color = 'cyan', edgecolor = 'k')
    plt.xlabel('Test(GRE)')
    plt.ylabel('Grades(GPA)')
    
# plot the points
plot_points(data)
plt.show()

#separate ranks
data_rank1 = data[data['rank']==1]
data_rank2 = data[data['rank']==2]
data_rank3 = data[data['rank']==3]
data_rank4 = data[data['rank']==4]

#plot each graph
plot_points(data_rank1)
plt.title("Rank 1")
plt.show()


plot_points(data_rank2)
plt.title("Rank 2")
plt.show()


plot_points(data_rank3)
plt.title("Rank 3")
plt.show()


plot_points(data_rank4)
plt.title("Rank 4")
plt.show()

# Make dummy variables for rank
one_hot_data = pd.get_dummies(data, columns=['rank'])
# Drop the previous rank column
one_hot_data = one_hot_data.drop(["rank"], axis = 1 )
one_hot_data[:5]

# Make a copy of the data
processed_data = one_hot_data[:]

# Scale the columns
processed_data['gpa'] /= 4.0
processed_data['gre'] /= 800

processed_data[:5]

sample = np.random.choice( processed_data.index, size =int(len(processed_data)*0.9), replace = False)
train_data, test_data = processed_data.iloc[sample], processed_data.drop(sample)

print("Number of training samples is", len(train_data))
print("Number of testing samples is", len(test_data))
print(train_data[:5])
print(test_data[:5])

features = train_data.drop('admit', axis=1)
targets = train_data['admit']
features_test = test_data.drop('admit', axis=1)
targets_test = test_data['admit']

print(features[:5])
print(targets[:5])

# Activation (sigmoid) function
def sigmoid(x):
    return 1/ (1+ np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

def error_formula(y, output):
    return -y* np.log(output) - (1-y) * np.log(1-output)

# Write the error term formula
def error_term_formula(x, y, output):
    return (y - output) * sigmoid_prime(x)

# Neural Network hyperparameters

epochs = 1000
learnrate = 0.5

# Training function
def train_nn( features, targets, epochs, learnrate):
    np.random.seed(42)
    n_records, n_features = features.shape
    last_loss = None
    
    # Initialize the weights
    weights = np.random.normal(scale=1 / n_features**.5, size = n_features)
    
    for e in range(epochs):
        del_w = np.zeros(weights.shape)
        for x, y in zip(features.values, targets):
            
            # Activation of the output unit
            output = sigmoid(np.dot(x, weights))
            
            # The error
            error = error_formula(y, output)
            
            # The error term
            error_term = error_term_formula(x,y,output)
            
            # The gradient descent step
            del_w += error_term * x
            
        # Update weights
        weights += learnrate * del_w / n_records
        
        # Print out the MSE on the training set
        if e % (epochs/10) == 0:
            out  = sigmoid(np.dot(features,weights))
            loss = np.mean((out - targets)**2)
            
            print("Epoch:", e)
            if last_loss and last_loss < loss:
                print("Train loss: ", loss, "  WARNING - Loss Increasing")
            else:
                print("Train loss: ", loss)
            
            last_loss = loss
            print("=========")
    print("Finished training!")
    return weights

    
# Call the training function
weights = train_nn(features, targets, epochs, learnrate)

test_out    = sigmoid(np.dot(features_test, weights))
predictions = test_out > 0.5
accuracy    = np.mean( predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))
