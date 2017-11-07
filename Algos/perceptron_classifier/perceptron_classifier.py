import pandas as pd
import tensorflow as tf
from sklearn.model_selection import StratifiedKFold

# Load Iris data
data = pd.read_csv('Algos/perceptron_classifier/iris.csv')
X_data = data.values[:,:-1]
y_data = pd.get_dummies(data['class'].values).values    #One-hot encoding

#Compute sizes
num_features = len(data.columns) - 1
num_classes = 3

#Define the neural network
X = tf.placeholder(tf.float32, [None, num_features]) #Input layer
W = tf.Variable(tf.zeros([num_features, num_classes])) #Weights
b = tf.Variable(tf.zeros([num_classes]))    #Biases
y = tf.nn.softmax(tf.matmul(X, W) + b) #Output layer

y_ = tf.placeholder(tf.float32, [None, num_classes]) #Output placeholder

#Cost function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

#Training step
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#Compute accuracy as a quality function
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#Initialize variables and start tensorflow session
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#Let's perform stratified k fold
kfold = 5  # need to change to 5
skf = StratifiedKFold(n_splits=kfold, random_state=0)
for i, (train_index, test_index) in enumerate(skf.split(X_data, data['class'].values)):
    sess.run(init) # reset values to wrong
    print('Batch: {} of {}: '.format(i + 1, kfold))
    X_train, X_test = X_data[train_index], X_data[test_index]
    y_train, y_test = y_data[train_index], y_data[test_index]
    for i in range(1000):
        sess.run(train_step, {X: X_train, y_: y_train})

    # evaluate training accuracy
    print("Accuracy: %s"%(sess.run(accuracy, {X: X_test, y_: y_test  })*100))
