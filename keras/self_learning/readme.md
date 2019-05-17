# Keras examples
## bigger_than25.py example
This program creates four arrays:
- x_train and x_test: **integer** input values between 0 and 50 for the neural network.
- y_train and y_test: **binary** output solution.

The condition to learn for the neural network is: 
- For inputs **bigger than 25 or equal** the solution is **1**.
- For inputs **smaller than 25** the solution is **0**.

Then the neural network train and predict.

### Results:
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

## alcohol.py example
This program loads data (acidity, sugar, density,  pH,  alcohol...) from two csv files that contains info about two types of wine, red and white.

Then creates and trains a sequential neural network model to predict the type of wine (red or white) using the loaded data as input.

### Results:
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

