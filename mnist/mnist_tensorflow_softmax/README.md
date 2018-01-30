# mnist_tensorflow_softmax

This is the "get started" of TensorFlow : [https://www.tensorflow.org/get_started/mnist/beginners](https://www.tensorflow.org/get_started/mnist/beginners)

Martin Görner, a Google Developer did a very good video for understand the basics of tensorflow with MNIST. Here is the link : [https://www.youtube.com/watch?v=vq2nnJ4g6N0](https://www.youtube.com/watch?v=vq2nnJ4g6N0) and his github : [https://github.com/martin-gorner/tensorflow-mnist-tutorial](https://github.com/martin-gorner/tensorflow-mnist-tutorial)

Good learning !

## Command line
```
python mnist_tensorflow_softmax.py
```
You need to have TensorFlow installed : [https://www.tensorflow.org/install/](https://www.tensorflow.org/install/)

## Results
With the simple Neural Network, we have cool results !
```
# WITH reduction_indices=[1]
# iterations = 10000
# learning_rate = 0.003
# => accuracy : 0.9255

# WITH reduction_indices=[1]
# iterations = 1000
# learning_rate = 0.03
# => accuracy : 0.8927

# WITH reduction_indices=[1]
# iterations = 1000
# learning_rate = 0.003
# => accuracy : 0.8335


# WITHOUT reduction_indices=[1]
# iterations = 10000
# learning_rate = 0.003
# => accuracy : 0.9239

# WITHOUT reduction_indices=[1]
# iterations = 1000
# learning_rate = 0.03
# => accuracy : 0.098 => NO TRAINING

# WITHOUT reduction_indices=[1]
# iterations = 1000
# learning_rate = 0.003
# => accuracy : 0.9175
```


## Questions
 * Why use the parameter 'reduction_indices=[1]' in the tf.reduce_sum ? And what it does ?
 * What does tf.argmax() ?
 * What does tf.reduce_mean() ?
 * What does tf.reduce_sum() ?
 * What does tf.cast() ?

