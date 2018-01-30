
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

import tensorflow as tf 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plot(samples):
    fig = plt.figure(figsize=(10, 10))
    gs = gridspec.GridSpec(10, 10)
    gs.update(wspace=0.0, hspace=0.0)

    for i, sample in enumerate(samples):
        ax = plt.subplot(gs[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('equal')
        plt.imshow(sample.reshape(28, 28), cmap='Greys')

    return fig

X = tf.placeholder(tf.float32, [None, 784])

# noise
Z = tf.placeholder(tf.float32, [None, 64])


# Discriminator
D_W1 = tf.Variable(tf.truncated_normal([784, 100], stddev=0.1))
D_B1 = tf.Variable(tf.zeros([100]))

D_W2 = tf.Variable(tf.truncated_normal([100, 1], stddev=0.1))
D_B2 = tf.Variable(tf.zeros([1]))

# Generator
G_W1 = tf.Variable(tf.truncated_normal([64, 100], stddev=0.1))
G_B1 = tf.Variable(tf.zeros([100]))

G_W2 = tf.Variable(tf.truncated_normal([100, 784], stddev=0.1))
G_B2 = tf.Variable(tf.zeros([784]))

theta_D = [D_W1, D_W2, D_B1, D_B2]
theta_G = [G_W1, G_W2, G_B1, G_B2]


def discriminator(X):
    D_h1 = tf.nn.relu( tf.matmul(X, D_W1) + D_B1)
    D_logits = tf.matmul(D_h1, D_W2) + D_B2
    
    D_prob = tf.nn.sigmoid(D_logits)

    return D_prob

def generator(Z):
    G_h1 = tf.nn.relu( tf.matmul(Z, G_W1) + G_B1)
    G_logits = tf.matmul(G_h1, G_W2) + G_B2

    G_prob = tf.nn.sigmoid(G_logits)

    return G_prob


G_sample = generator(Z)

D_real_prob = discriminator(X)
D_fake_prob = discriminator(G_sample)


def log(x):
    return tf.log(x + 1e-6)

# Loss
D_loss = -tf.reduce_mean(log(D_real_prob) + log(1. - D_fake_prob))
G_loss = -tf.reduce_mean(log(D_fake_prob))

# Train
# What is var_list ? Without var_list, the model learns nothing !!!!
# var_list: Optional list or tuple of Variable objects to update to minimize loss. Defaults to the list of variables collected in the graph under the key GraphKeys.TRAINABLE_VARIABLES.

# I have the feeling that it was able to understand the link and change the variables itself...
# But in fact, it can't to do that because it depends of Variables
# I can only change specific variables to updates the loss
# Without that, it is able to reduce the precision of the discriminator to have a better generator

# If var_list = None, takes it every variables ?
# If I only put that for a simple training : train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy, var_list=[B])
# I have no really train, I am always to 0.1135 of accuracy. In random, I am to 0.1
D_solver = tf.train.AdamOptimizer(0.001).minimize(D_loss, var_list=theta_D)
G_solver = tf.train.AdamOptimizer(0.001).minimize(G_loss, var_list=theta_G)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

def sample_z(m, n):
    return np.random.uniform(-1., 1., size=[m, n])

i = 0

for it in range(1000000):
    batch_xs, _ = mnist.train.next_batch(100)
    Z_gen = sample_z(100, 64)

    sess.run([D_solver], feed_dict={X: batch_xs, Z: Z_gen})
    sess.run([G_solver], feed_dict={X: batch_xs, Z: Z_gen})

    print(it)

    if it % 1000 == 0:
        samples = sess.run(G_sample, feed_dict={Z: sample_z(100, 64)})
        fig = plot(samples)
        plt.savefig('out/{}.png'.format(str(i).zfill(3)), bbox_inches='tight')
        i += 1
        plt.close(fig)