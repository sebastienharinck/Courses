# notMNIST_speed_test

notMNIST is a dataset of pictures of letters. The goal is simple : recognize the letter of these images.

![alt text](http://yaroslavvb.com/upload/notMNIST/nmn.png)

Of course, my code and my model suck ! But it is a good "first step" for checking if you can do something very quick with a new dataset. This model is not perfect but learn something.

I did this code because of this article : [https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb)

But I didn't read it because I wanted to check if I was able to create this model on my own. 

## Requirement for understand this code

If you are a beginner in Machine Learning (like me), I recommend you to learn this course first : [https://www.tensorflow.org/get_started/mnist/beginners](https://www.tensorflow.org/get_started/mnist/beginners)

Martin Görner, a Google Developer did a very good video for understand the basics of tensorflow with MNIST. Here is the link : [https://www.youtube.com/watch?v=vq2nnJ4g6N0](https://www.youtube.com/watch?v=vq2nnJ4g6N0) and his github : [https://github.com/martin-gorner/tensorflow-mnist-tutorial](https://github.com/martin-gorner/tensorflow-mnist-tutorial)

Good learning !

## Command line

Normally, you can launch this script with one command line :

```
python notMNIST_speed_test.py
```
You need to have TensorFlow installed : [https://www.tensorflow.org/install/](https://www.tensorflow.org/install/)

## Improvements

Lot of things can be done for improve this model. Here are my few ideas :
 * TODO 01 : seperate train and test
 * TODO 02 : do read_data_sets('NotMNIST_data', one_hot=True, reshape=False) like MNIST on TensorFlow
 * TODO 03 : do a version without tensorflow
 * TODO 04 : OO
 * TODO 05 : seperate the code in many files
 * TODO 06 : train with 5 layers
 * TODO 07 : train with CNN layers
 * TODO 08 : generate one_hot on label
 * TODO 09 : add tensorboard
 * TODO 10 : do the same with notMNIST in big
 * TODO 11 : create a GAN Model for generate new letter
 * TODO 12 : improve next_batch()

Feel free to share your ideas with me :)

