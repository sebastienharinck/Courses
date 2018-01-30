# TODO 01 : seperate train and test
# TODO 02 : do read_data_sets('NotMNIST_data', one_hot=True, reshape=False) like MNIST on TensorFlow
# TODO 03 : do a version without tensorflow
# TODO 04 : OO
# TODO 05 : seperate the code in many files
# TODO 06 : train with 5 layers
# TODO 07 : train with CNN layers
# TODO 08 : generate one_hot on label

# TODO 09 : add tensorboard
# TODO 10 : do the same with notMNIST in big
# TODO 11 : create a GAN Model for generate new letter
# TODO 12 : improve next_batch()

# read an image with pixels
from PIL import Image
import os
import io
import random
import urllib.request
import sys
import tarfile

def getFileNameFromUrl(url):
	return url.split('/')[-1]

def downloadURLFile(url, file_name=''):
	if not file_name:
		file_name = getFileNameFromUrl(url)

	if not os.path.isfile(file_name):
		print('Download...')
		response = urllib.request.urlretrieve(url, file_name)

def getNotMNIST_small():	
	url = 'http://yaroslavvb.com/upload/notMNIST/notMNIST_small.tar.gz'
	file_name = getFileNameFromUrl(url)

	downloadURLFile(url, file_name)
	extractFile(file_name)

def extractFile(file_name):
	if (file_name.endswith("tar.gz")):
		print('Extract...')
		tar = tarfile.open(file_name, "r:gz")
		tar.extractall()
		tar.close()

def getPixelsOfImg(path):	
	try:
		im = Image.open(repository_imgs + path)   
	except IOError:
		return False

	pixels = list(im.getdata())
	return pixels

def getLabelOfImg(path):
	return path[0]

def getOneHot(label):
	labels_one_hot = {
		'A': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		'B': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		'C': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		'D': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		'E': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		'F': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		'G': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
		'H': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		'I': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		'J': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	}

	return labels_one_hot[label]

def next_batch(size=100):
	i = 0
	batch_xs = []
	batch_ys = []

	while i < size:
		label = random.choice(labels)
		img_name = random.choice(os.listdir(repository_imgs + label))
		path_img = label + '/' + img_name

		img_pixels = getPixelsOfImg(path_img)

		if img_pixels:
			label = getLabelOfImg(path_img)
			img_label_vector = getOneHot(label)

			batch_xs.append(img_pixels)
			batch_ys.append(img_label_vector)

			i += 1

	return batch_xs, batch_ys

# Specific 
# Download
repository_imgs = 'notMNIST_small/'
if not os.path.isdir(repository_imgs):
	getNotMNIST_small()

labels = ['A','B','C','D','E','F','G','H','I','J',]


# MODEL
import tensorflow as tf

X = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784, 10]))
B = tf.Variable(tf.zeros([10]))

Ylogits = tf.matmul(X, W) + B

Y = tf.nn.softmax( Ylogits )

Y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels=Y_, logits=Ylogits))
train_step = tf.train.AdamOptimizer(0.03).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

correct_prediction = tf.equal( tf.argmax(Y, 1), tf.argmax(Y_, 1))
accuracy = tf.reduce_mean( tf.cast(correct_prediction, tf.float32 ))

for i in range(1000):
 	batch = next_batch(100)
 	if not batch:
 		break
 	acc = accuracy.eval(feed_dict={X: batch[0], Y_: batch[1]})
 	print('step %d -> accuracy : %g' %(i, acc))

 	sess.run(train_step, feed_dict={X: batch[0], Y_: batch[1]})


# For testing at the beginning
# def showAll():
# 	i = 0
# 	for repository_label in os.listdir(repository_imgs):
# 		for img in os.listdir(repository_imgs + repository_label):
# 			path_img = repository_label + '/' + img
			
# 			pixels = getPixelsOfImg(path_img)

# 			if pixels:
# 				label = getLabelOfImg(path_img)
# 				img_label_vector = getOneHot(label)

# 				print(pixels)
# 				print(label)
# 				print(img_label_vector)
# 				i += 1

# 	print(i)