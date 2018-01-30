
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

import tensorflow as tf

# Images
X = tf.placeholder(tf.float32, [None, 784])

# Weights
W = tf.Variable(tf.zeros([784, 10]))
B = tf.Variable(tf.zeros([10]))

# Softmax
Y = tf.nn.softmax( tf.matmul(X, W) + B )

# Labels
Y_ = tf.placeholder(tf.float32, [None, 10])

# Parameters
learning_rate = 0.03
iterations = 1000

# Cross entropy
# cross_entropy = tf.reduce_mean( - tf.reduce_sum( Y_ * tf.log(Y)) )
cross_entropy = tf.reduce_mean( - tf.reduce_sum( Y_ * tf.log(Y), reduction_indices=[1] ) )

train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()


# Training
for _ in range(iterations):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={X: batch_xs, Y_: batch_ys})


# Evaluation
correct_prediction = tf.equal( tf.argmax(Y, 1), tf.argmax(Y_, 1) )
accuracy = tf.reduce_mean( tf.cast(correct_prediction, tf.float32) )
print(sess.run(accuracy, feed_dict={X: mnist.test.images, Y_: mnist.test.labels}))
