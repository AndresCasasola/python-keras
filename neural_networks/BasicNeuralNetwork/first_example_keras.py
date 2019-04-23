
# Importing libraries
import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

# Preprocessing Data
train_labels = []
train_samples =[]

for i in range(5):
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_labels.append(0)
    
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_labels.append(1)

for i in range(5):
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_labels.append(1)
    
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_labels.append(0)

for i in train_samples:
    print(i)

for i in train_labels:
    print(i)

train_labels = np.array(train_labels)
train_samples = np.array(train_samples)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform((train_samples).reshape(-1,1))

for i in scaled_train_samples:
    print(i)

# Creating network
model = Sequential([
    Dense(16, input_shape=(1,), activation = 'relu'),
    Dense(32, activation = 'relu'),
    Dense(2, activation = 'softmax'),
    
])

model.summary()

# Training network
model.compile(Adam(lr=.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(scaled_train_samples, train_labels, validation_split = 0.1, batch_size=10, epochs=20, shuffle=True, verbose=2)

# Predicting
predictions = model.predict(scaled_train_samples, batch_size=10, verbose=0)

for i in predictions:
    print(i)

rounded_predictions = model.predict_classes(scaled_train_samples, batch_size=10, verbose=0)

for i in rounded_predictions:
    print(i)

