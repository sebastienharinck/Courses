# mnist_simple_gan
The most simple Generative Adversarial Nets for MNIST.

It is inspired of : [http://wiseodd.github.io/techblog/2016/09/17/gan-tensorflow/](http://wiseodd.github.io/techblog/2016/09/17/gan-tensorflow/)

The goal of this model is to generate handwritten digits. You can see the results at the bottom.

## Problem

The generator can find a way to "win" vs the discriminator with one example and doesn't try something else. Like this one :

We can see that after 99 generations. The generator is only good to generate "8" and "9" digits...

## Questions

 - How to generate images with all labels (0 to 9) ?


## Results

<p align="center">
first generation : no training -> just noise
<img src="https://raw.githubusercontent.com/sebastienharinck/mnist_simple_gan/master/doc/000.png">
</p>

<p align="center">
after 10 generations
<img src="https://raw.githubusercontent.com/sebastienharinck/mnist_simple_gan/master/doc/010.png">
</p>

<p align="center">
after 99 generations
<img src="https://raw.githubusercontent.com/sebastienharinck/mnist_simple_gan/master/doc/099.png">
</p>
