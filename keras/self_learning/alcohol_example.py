###########################################################
#
# - Description: This example  takes  data (acidity, sugar, 
#   density,  pH,  alcohol...)  from  diferents  wines  and
#   creates and trains a sequential neural network model to
#   predict the type of wine (red or white) using this data
#   as input.
#
# - This code has been modified from the original.
# - The original  one  was extracted  from "Keras Tutorial: 
#   Deep Learning in Python", writen  by Karlijn Willems in
#   2019. Uploaded in www.datacamp.com.
#
# - Modifications by: Andres Casasola Dominguez.
#
###########################################################


########## Loading data
# Import pandas
import pandas as pd

# Read in white wine data 
white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
# Read in red wine data 
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

########## Data exploration
# Print info on white wine
#print(white.info())
# Print info on red wine
#print(red.info())

########## Show raw data
"""
# First rows of `red` 
red.head(5)
# Last rows of `white`
white.tail()
# Take a sample of 5 rows of `red` (aleatory)
red.sample(5)
# Describe `white`
white.describe()
# Double check for null values in `red`
pd.isnull(red)
"""
########## Plot data statistics
"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

ax[0].hist(red.alcohol, 10, facecolor='red', alpha=0.5, label="Red wine")
ax[1].hist(white.alcohol, 10, facecolor='white', ec="black", lw=0.5, alpha=0.5, label="White wine")

fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=1)
ax[0].set_ylim([0, 1000])
ax[0].set_xlabel("Alcohol in % Vol")
ax[0].set_ylabel("Frequency")
ax[1].set_xlabel("Alcohol in % Vol")
ax[1].set_ylabel("Frequency")
#ax[0].legend(loc='best')
#ax[1].legend(loc='best')
fig.suptitle("Distribution of Alcohol in % Vol")

plt.show()
"""
########## Preprocess data
# Add `type` column to `red` with value 1
red['type'] = 1
# Add `type` column to `white` with value 0
white['type'] = 0
# Append `white` to `red`
wines = red.append(white, ignore_index=True)

########## Train and test
# Import `train_test_split` from `sklearn.model_selection`
from sklearn.model_selection import train_test_split
import numpy as np
# (Input values) Specify the data (takes all rows and 0 to 11 columns) 
X=wines.ix[:,0:11]
# (Output values) Specify the target labels and flatten the array 
y=np.ravel(wines.type)
# Split the data up in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

########## Standardize data (Scale/normalize data)
# Import `StandardScaler` from `sklearn.preprocessing`
from sklearn.preprocessing import StandardScaler
# Define the scaler 
scaler = StandardScaler().fit(X_train)
# Scale the train set
X_train = scaler.transform(X_train)
# Scale the test set
X_test = scaler.transform(X_test)

########## Creating neural network model
# Import `Sequential` from `keras.models`
from keras.models import Sequential
# Import `Dense` from `keras.layers`
from keras.layers import Dense
# Initialize the constructor (Sequential model is multilayer perceptron)
model = Sequential()
# Add an input layer
# |Dense: neurons fully connected | activation='relu': 
model.add(Dense(12, activation='relu', input_shape=(11,))) # input_shape=(*, 11)
# Add one hidden layer 
model.add(Dense(8, activation='relu'))
# Add an output layer 
model.add(Dense(1, activation='sigmoid'))

########## Model information
# Model output shape
model.output_shape
# Model summary
model.summary()
# Model config
#model.get_config()
# List all weight tensors 
#model.get_weights()

########## Compile and Fit
# Compile model with adam optimizer and binary_crossentropy for loss function.
# Select accuracy as metrics to monitorize it during the training.
# binary_crossentropy is for binary classification problems. If the classification
# is with multiclass must be used categorical_crossentropy.
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# Fit the model during 20 epochs. Batch size is the number of samples that will be 
# propagated through the network every epoch.
model.fit(X_train, y_train,epochs=1, batch_size=1, verbose=1)

########## Predict
y_pred = model.predict(X_test)

print(y_pred[:10])
print(y_test[:10])

########## Evaluate model
score = model.evaluate(X_test, y_test,verbose=1)
print('Evaluation loss:', score[0])
print('Evaluation accuracy:', score[1])


