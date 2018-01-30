
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True, reshape=False)

import tensorflow as tf 

X = tf.placeholder(tf.float32, [None, 28, 28, 1])
Y_ = tf.placeholder(tf.float32, [None, 10])

K = 8
L = 16
M = 24

W1 = tf.Variable(tf.truncated_normal([6, 6, 1, K], stddev=0.1))
B1 = tf.Variable(tf.zeros([K]))

W2 = tf.Variable(tf.truncated_normal([6, 6, K, L], stddev=0.1))
B2 = tf.Variable(tf.zeros([L]))

W3 = tf.Variable(tf.truncated_normal([5, 5, L, M], stddev=0.1))
B3 = tf.Variable(tf.zeros([M]))

W4 = tf.Variable(tf.truncated_normal([7*7*M, 200], stddev=0.1))
B4 = tf.Variable(tf.zeros([200]))

W5 = tf.Variable(tf.truncated_normal([200, 10], stddev=0.1))
B5 = tf.Variable(tf.zeros([10]))


Y1 = tf.nn.relu( tf.nn.conv2d(X, W1, strides=[1, 1, 1, 1], padding='SAME') + B1)
Y2 = tf.nn.relu( tf.nn.conv2d(Y1, W2, strides=[1, 2, 2, 1], padding='SAME') + B2)
Y3 = tf.nn.relu( tf.nn.conv2d(Y2, W3, strides=[1, 2, 2, 1], padding='SAME') + B3)

Y3_flat = tf.reshape(Y3, [-1, 7*7*M])

Y4 = tf.nn.relu( tf.matmul(Y3_flat, W4) + B4 )
Ylogits = tf.matmul(Y4, W5) + B5

Y = tf.nn.softmax( Ylogits)

cross_entropy = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels=Y_, logits=Ylogits) )
train_step = tf.train.AdamOptimizer(0.003).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

correct_prediction = tf.equal( tf.argmax(Y, 1), tf.argmax(Y_, 1) )
accuracy = tf.reduce_mean( tf.cast(correct_prediction, tf.float32) )

for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	acc = accuracy.eval(feed_dict={X: batch_xs, Y_: batch_ys})
	print('step %d, accuracy -> %g'%(i, acc))

	sess.run(train_step, feed_dict={X: batch_xs, Y_: batch_ys})

print(accuracy.eval(feed_dict={X: mnist.test.images, Y_: mnist.test.labels}))
