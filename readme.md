# Some python code

## [*Cifar 10*](https://github.com/AndresCasasola/python-keras/raw/master/keras/self_learning) keras example
##### Training to recognize images

This program takes data from cifar10 dataset with 50.000 training and 10.000 testing samples of 32x32 images with 10 categories (frog, dog, truck, car...).
Then creates a sequential neural network model to predict the category of each image.

#### Results:
##### Parameters used:
- Training epochs: 50
- Batch size: 32
- Steps per epoch: 1000
- Evaluation samples: 200

##### Model training:

![Figure 2](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/acc72_data.png "Figure 2")


##### Evaluation:

![Figure 10](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/cifar10_evaluation.png "Figure 10")

##### Results:

![Figure 10](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/cifar10_images.png "Figure 10")

*Predictions* are the values calculed by the neural network and *Solutions* are the correct values from the dataset.

![Figure 11](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/cifar10_results.png "Figure 11")
