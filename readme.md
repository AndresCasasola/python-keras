# Some python code

## cifar10.py example in keras/self_learning

This program takes data from cifar10 dataset with 50.000 training and 10.000 testing samples of 32x32 images with 10 categories (frog, dog, truck, car...).
Then creates a sequential neural network model to predict the category of each image.

### Results:

In my results i did not train the model (computer not powerful enough), instead i loaded the file *keras_cifar10_trained_model.h5* that contains the weights of a trained model with 78% accuracy.

##### Evaluation:

![Figure 10](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/cifar10_evaluation.png "Figure 10")

##### Results:

![Figure 10](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/cifar10_images.png "Figure 10")

*Predictions* are the values calculed by the neural network and *Solutions* are the correct values from the dataset.

![Figure 11](https://github.com/AndresCasasola/python-keras/raw/master/resources/images/cifar10_results.png "Figure 11")
