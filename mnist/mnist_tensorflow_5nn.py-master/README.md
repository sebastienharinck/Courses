# mnist_tensorflow_5nn.py

![alt text](https://raw.githubusercontent.com/GarryMorrison/Feynman-knowledge-engine/master/work-on-images/mnist-100-images.jpg)

MNIST with 5 layers. You can see the results at the end of the README.md with many parameters.

This is the "get started" of TensorFlow : [https://www.tensorflow.org/get_started/mnist/beginners](https://www.tensorflow.org/get_started/mnist/beginners)

Martin Görner, a Google Developer did a very good video for understand the basics of tensorflow with MNIST. Here is the link : [https://www.youtube.com/watch?v=vq2nnJ4g6N0](https://www.youtube.com/watch?v=vq2nnJ4g6N0) and his github : [https://github.com/martin-gorner/tensorflow-mnist-tutorial](https://github.com/martin-gorner/tensorflow-mnist-tutorial)

Good learning !

## Command line
```
python mnist_tensorflow_5nn.py
```
You need to have TensorFlow installed : [https://www.tensorflow.org/install/](https://www.tensorflow.org/install/)

## Results
With the simple Neural Network, we have cool results !
```
# K = 200

# iterations = 1000
# learning rate = 0.03
# train accuracy : 0.9298
# test accuracy : 0.9256

# Overfitting ?
# iterations = 10000
# learning rate = 0.03
# train accuracy : 0.284145
# test accuracy : 0.2811

# iterations = 10000
# learning rate = 0.003
# train accuracy : 0.996255
# test accuracy : 0.9759

# At the end, train accuracy is always 1. So the model is able to save everything no ?
# iterations = 100000
# learning rate = 0.003
# train accuracy : 0.997455
# test accuracy : 0.9778


# K = 2000

# iterations = 1000
# learning rate = 0.03
# train accuracy : 0.943036
# test accuracy : 0.9425

# iterations = 10000
# learning rate = 0.003
# train accuracy : 0.9958
# test accuracy : 0.9782


# K = 20000 (very long...)

# iterations = 1000
# learning rate = 0.03
# train accuracy : 0.626564
# test accuracy : 0.6287

# iterations = 10000
# learning rate = 0.003
# train accuracy : 0.997945
# test accuracy : 0.9845

```
