from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

import tensorflow as tf 

X = tf.placeholder(tf.float32, [None, 784])

K = 200
L = 100
M = 60
N = 30

W1 = tf.Variable(tf.truncated_normal([784, K], stddev=0.1))
B1 = tf.Variable(tf.zeros([K]))

W2 = tf.Variable(tf.truncated_normal([K, L], stddev=0.1))
B2 = tf.Variable(tf.zeros([L]))

W3 = tf.Variable(tf.truncated_normal([L, M], stddev=0.1))
B3 = tf.Variable(tf.zeros([M]))

# If W1, W2, W3 and W4 are initialized with tf.zeros, there is no possibility of learning !
W4 = tf.Variable(tf.truncated_normal([M, N], stddev=0.1))
B4 = tf.Variable(tf.zeros([N]))

W5 = tf.Variable(tf.zeros([N, 10]))
B5 = tf.Variable(tf.zeros([10]))

# Works with sigmoid too
Y1 = tf.nn.relu( tf.matmul(X, W1) + B1 )
Y2 = tf.nn.relu( tf.matmul(Y1, W2) + B2 )
Y3 = tf.nn.relu( tf.matmul(Y2, W3) + B3 )
Y4 = tf.nn.relu( tf.matmul(Y3, W4) + B4 )
Ylogits = tf.matmul(Y4, W5) + B5

Y = tf.nn.softmax( Ylogits )

Y_ = tf.placeholder(tf.float32, [None, 10])

iterations = 1000
learning_rate = 0.03

cross_entropy = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels=Y_, logits=Ylogits) )
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

correct_prediction = tf.equal( tf.argmax(Y, 1), tf.argmax(Y_, 1) )
accuracy = tf.reduce_mean( tf.cast(correct_prediction, tf.float32) )

for i in range(iterations):
	batch_xs, batch_ys = mnist.train.next_batch(100)

	acc = accuracy.eval(feed_dict={X: batch_xs, Y_: batch_ys})
	print('step %d : accuracy -> %g' %(i, acc))

	sess.run(train_step, feed_dict={X: batch_xs, Y_: batch_ys})

print('FINAL TRAIN ACCURACY :')
print(accuracy.eval(feed_dict={X: mnist.train.images, Y_: mnist.train.labels}))

print('FINAL TEST ACCURACY :')
print(accuracy.eval(feed_dict={X: mnist.test.images, Y_: mnist.test.labels}))