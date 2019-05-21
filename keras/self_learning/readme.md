# Keras examples

## [*Cifar 10*](https://github.com/AndresCasasola/python-keras/raw/master/keras/self_learning)
##### Training to recognize images

##### Description:

This program takes data from cifar10 dataset with 50.000 training and 10.000 testing samples of 32x32 images with 10 categories (frog, dog, truck, car...).
Then creates a sequential neural network model to predict the category of each image.

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

## *Biggerthan25*
##### Description:
This program creates four arrays:
- *x_train* and *x_test*: **integer** input values between 0 and 50.
- *y_train* and *y_test*: **binary** output solution.

The condition to learn for the neural network is: 
- For inputs **bigger than 25 or equal** the solution is **1**.
- For inputs **smaller than 25** the solution is **0**.
- Example:
    - *x_train = 30* | *y_train = 1*
    - *x_train = 20* | *y_train = 0*

Then the neural network train and predict.

##### Parameters used:
- Training epochs: 20
- Batch size: 10
- Samples: 10000

##### Model summary:

![Figure 1](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/biggerthan25_model_summary.png "Figure 1")

##### Model training:

![Figure 2](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/biggerthan25_training.png "Figure 2")

##### Results:

![Figure 3](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/biggerthan25_results.png "Figure 3")

## *Wine*
##### Description:
This program loads data (acidity, sugar, density,  pH,  alcohol...) from two csv files that contains info about two types of wine, red and white.

Then creates and trains a sequential neural network model to predict the type of wine (red or white) using the loaded data as input.

##### Parameters used:
- Training epochs: 10
- Batch size: 1

##### Wine information loaded:
- White wine:

![Figure 4](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/alcohol_whiteinfo.png "Figure 4")
- Red wine:

![Figure 5](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/alcohol_redinfo.png "Figure 5")

##### Model summary:

![Figure 6](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/alcohol_model_summary.png "Figure 6")

##### Model training:

![Figure 7](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/alcohol_training.png "Figure 7")

##### Evaluation:

![Figure 8](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/alcohol_evaluation.png "Figure 8")

##### Results:

![Figure 9](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/alcohol_results.png "Figure 9")





